# Generated by Django 4.0.2 on 2022-02-10 16:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0003_patient_delete_backenddata_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='patient_history',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
