from django.shortcuts import render

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
        with open(obj.file_name.path, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f, delimiter=";")
            for row1 in reader:
                season = row1[0]
                bonus = season + 'B'
                single, _ = Player.objects.update_or_create(
                    name=row1[1],
                    defaults={
                        **{season: row1[2] if row1[2] else 0, },
                        **{bonus: row1[3] + row1[4] if row1[4] or row1[4] else 0, },
                        },
                )
            obj.activated = True
            obj.save()
    return render(request, 'leaderboard/upload.html', {'form': form})
