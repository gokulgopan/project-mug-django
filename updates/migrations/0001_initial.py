# Generated by Django 2.2.1 on 2019-05-27 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Updates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter the Title', max_length=50)),
                ('date_pub', models.DateTimeField(verbose_name='Date Published')),
            ],
        ),
    ]
