# Generated by Django 4.0.3 on 2022-03-28 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_clientdocumentdatamodel_clientdocumenteventdatamodel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientdocumentrequestdatamodel',
            name='encoded_client_document_request_id',
            field=models.CharField(default='pfGKOs83bqB0ajSZ47oVDpvGSxmgDHcD', max_length=32),
        ),
    ]
