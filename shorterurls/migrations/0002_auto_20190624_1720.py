# Generated by Django 2.2.2 on 2019-06-24 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shorterurls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='storedurls',
            old_name='url_after_short',
            new_name='full_url',
        ),
        migrations.RenameField(
            model_name='storedurls',
            old_name='url_before_short',
            new_name='short_url',
        ),
    ]
