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
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    pass
                else:
                    for row in reader:
                        single, _ = Player.objects.get_or_create(
                            name=row[1],
                            event01=row[2],
                            event02=row[3],
                            event03=row[4],
                            event04=row[5],
                            event05=row[6],
                            event06=row[7],
                            event07=row[8],
                            event08=row[9],
                            event09=row[10],
                            event10=row[11],
                            event11=row[12],
                            event12=row[13],
                        )
            obj.activated = True
            obj.save()
    return render(request, 'leaderboard/upload.html', {'form': form})
