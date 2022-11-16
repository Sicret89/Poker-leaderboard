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
                            S1E1=row[1],
                            S1E2=row[2],
                            S1E3=row[3],
                            S1E4=row[4],
                            S1E5=row[5],
                            S1E6=row[6],
                            S1E7=row[7],
                            S1E8=row[8],
                            S1E9=row[9],
                            S1E10=row[10],
                            S1E11=row[11],
                            S1E12=row[12],
                        )
            obj.activated = True
            obj.save()
    return render(request, 'leaderboard/upload.html', {'form': form})
