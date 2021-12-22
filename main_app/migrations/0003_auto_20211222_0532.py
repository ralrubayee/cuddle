# Generated by Django 3.2.9 on 2021-12-22 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_remove_tips_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='milestone',
            options={'ordering': ['-date']},
        ),
        migrations.RemoveField(
            model_name='photo',
            name='cat',
        ),
        migrations.AddField(
            model_name='photo',
            name='milestone',
            field=models.OneToOneField(default=3, on_delete=django.db.models.deletion.CASCADE, to='main_app.milestone'),
            preserve_default=False,
        ),
    ]
