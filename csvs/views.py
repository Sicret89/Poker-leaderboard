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
                            E1=row[1],
                            E2=row[2],
                            E3=row[3],
                            E4=row[4],
                            E5=row[5],
                            E6=row[6],
                            E7=row[7],
                            E8=row[8],
                            E9=row[9],
                            E10=row[10],
                            E11=row[11],
                            E12=row[12],
                        )
            obj.activated = True
            obj.save()
    return render(request, 'leaderboard/upload.html', {'form': form})
