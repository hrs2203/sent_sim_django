# Generated by Django 3.2.4 on 2021-10-14 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_component', '0004_rename_quert_count_userhistory_query_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='saved_query_file',
            field=models.CharField(default='', max_length=200),
        ),
    ]