from django.shortcuts import render

from leaderboard.models import SingleTournament, Tournament
from .models import Csv
from .forms import  CsvModelForm
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
                if i==0:
                    pass
                else:
                    for row in reader:
                        single, _ = SingleTournament.objects.get_or_create(
                            player=row[1],
                            points=row[2],
                            bonus_a=row[3],
                            bonus_b=row[4],
                        )
                        seasons = row[0]
                        for season in seasons:
                            name, _ = Tournament.objects.get_or_create(name=seasons)
                            single.season.add(name)
            obj.activated = True
            obj.save()
    return render(request, 'leaderboard/upload.html', {'form': form})