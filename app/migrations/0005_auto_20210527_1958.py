# Generated by Django 3.2.3 on 2021-05-27 13:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0004_alter_house_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='users_id',
        ),
        migrations.AddField(
            model_name='house',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='users.user'),
            preserve_default=False,
        ),
    ]
