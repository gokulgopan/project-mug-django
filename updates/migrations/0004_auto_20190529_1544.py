# Generated by Django 2.2.1 on 2019-05-29 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('updates', '0003_auto_20190528_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='update',
            name='body',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='update',
            name='title',
            field=models.CharField(help_text='Enter the Title', max_length=100),
        ),
    ]
