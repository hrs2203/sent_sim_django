# Generated by Django 3.2.4 on 2021-11-08 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_component', '0007_historysentence'),
    ]

    operations = [
        migrations.AddField(
            model_name='userhistory',
            name='comp_type',
            field=models.CharField(default='CUSTOM', max_length=200),
        ),
    ]