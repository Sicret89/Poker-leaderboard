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
                            name=row[0],
                            event01=row[1],
                            event02=row[2],
                            event03=row[3],
                            event04=row[4],
                            event05=row[5],
                            event06=row[6],
                            event07=row[7],
                            event08=row[8],
                            event09=row[9],
                            event10=row[10],
                            event11=row[11],
                            event12=row[12],
                        )
            obj.activated = True
            obj.save()
    return render(request, 'leaderboard/upload.html', {'form': form})
