# Generated by Django 4.0.3 on 2022-03-28 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_clientdocumentrequestdatamodel_encoded_client_document_request_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelationshipManagerEmailIdentityDataModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relationship_manager_id', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('update_ts', models.DateTimeField(auto_now=True)),
                ('update_by', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='clientdocumentdatamodel',
            name='client_document_request_id',
        ),
        migrations.AddField(
            model_name='clientdocumentdatamodel',
            name='relationship_manager_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clientdocumentrequestdatamodel',
            name='encoded_client_document_request_id',
            field=models.CharField(default='mYkO3PL1PdZelUOWdCXYt1PIj25UHOOU', max_length=32),
        ),
    ]