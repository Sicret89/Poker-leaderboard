import os
import boto3
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
        s3 = boto3.client('s3')
        bucket = os.environ.get('AWS_STORAGE_BUCKET_NAME')
        result = s3.list_objects(Bucket=bucket, Prefix='/csvs/')
        print(result)
        # for o in result.get('Contents'):
        #     data = s3.get_object(Bucket=bucket, Key=o.get('Key'))
        #     contents = data['Body'].read()
        #     print(contents.decode("utf-8"))
        with open(obj.file_name.name, 'r', encoding='utf-8-sig') as f:
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
    return render(request, 'leaderboard/upload.html', {'form': form})
