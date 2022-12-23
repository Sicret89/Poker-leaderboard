from django.core.exceptions import FieldError
from django.contrib import messages
from django.core.files.storage import default_storage as storage
from django.shortcuts import render
import logging

from leaderboard.models import Player
from .models import Csv
from .forms import CsvModelForm
import csv

def upload_file_view(request):
    form = CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvModelForm()
        obj = Csv.objects.get(activated=False)
        with storage.open(obj.file_name.name, 'r') as f:
            try:
                reader = csv.reader(f, delimiter=";")
                for row1 in reader:
                    season = row1[0]
                    bonus_ak = season + 'B_AK'
                    bonus_47 = season + 'B_47'
                    jocker = season + '_JOCKER'
                    single, _ = Player.objects.update_or_create(
                        name=row1[1],
                        defaults={
                            **{season: row1[2] if row1[2] else 0, },
                            **{bonus_ak: row1[3] if row1[3] else 0, },
                            **{bonus_47: row1[4] if row1[4] else 0, },
                            **{jocker: row1[6] if row1[6] else None, },
                        },
                    )
                obj.activated = True
                obj.save()
                messages.success(request, 'File upload successful')
            except (FieldError, IndexError) as e:
                obj.delete()
                messages.warning(request, f'File upload failed: {e}')
                logging.exception('')
    return render(request, 'leaderboard/upload.html', {'form': form})
