# Generated by Django 4.0.3 on 2022-03-29 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_clientdocumentdatamodel_client_document_request_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientdocumentdatamodel',
            name='description',
            field=models.CharField(default='Client document', max_length=300),
        ),
        migrations.AlterField(
            model_name='clientdocumentrequestdatamodel',
            name='encoded_client_document_request_id',
            field=models.CharField(default='ZSwKa7R5JJYk7V9HXCE5nE1xdc9pNJf8', max_length=32),
        ),
    ]
