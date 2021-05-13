# Generated by Django 2.2 on 2021-05-13 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ninja',
            name='dojo',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='ninjas', to='dojo_ninjas_app.Dojo'),
            preserve_default=False,
        ),
    ]
