# Generated by Django 3.2.7 on 2021-12-01 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_tips_catgory_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='tips',
            name='catgory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.tips_catgory'),
            preserve_default=False,
        ),
    ]
