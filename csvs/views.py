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
        with open(obj.file_name.path, 'r', encoding='cp1252') as f:
            reader = csv.reader(f, delimiter=";")
            Player.objects.all().delete()
            for i, row1 in enumerate(reader):
                if i <= 2:
                    pass
                else:
                    for row1 in reader:
                        single, _ = Player.objects.get_or_create(
                            name=row1[1],
                            E1=row1[2] if row1[2] else 0,
                            E2=row1[3] if row1[3] else 0,
                            E3=row1[4] if row1[4] else 0,
                            E4=row1[5] if row1[5] else 0,
                            E5=row1[6] if row1[6] else 0,
                            E6=row1[7] if row1[7] else 0,
                            E7=row1[8] if row1[8] else 0,
                            E8=row1[9] if row1[9] else 0,
                            E9=row1[10] if row1[10] else 0,
                            E10=row1[11] if row1[11] else 0,
                            E11=row1[12] if row1[12] else 0,
                            E12=row1[13] if row1[13] else 0,
                        )
            obj.activated = True
            obj.save()
    return render(request, 'leaderboard/upload.html', {'form': form})
