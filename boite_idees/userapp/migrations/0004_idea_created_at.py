# Generated by Django 4.1.7 on 2023-03-24 14:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0003_voter_vote_alter_voter_unique_together_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]