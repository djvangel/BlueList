# Generated by Django 4.0.1 on 2022-02-04 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('titulos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='titulo',
            old_name='imagen1',
            new_name='imagen',
        ),
        migrations.RemoveField(
            model_name='personaje',
            name='selec_interprete1',
        ),
        migrations.RemoveField(
            model_name='personaje',
            name='selec_interprete2',
        ),
        migrations.RemoveField(
            model_name='personaje',
            name='selec_interprete3',
        ),
        migrations.RemoveField(
            model_name='personaje',
            name='titulo_interprete1',
        ),
        migrations.RemoveField(
            model_name='personaje',
            name='titulo_interprete2',
        ),
        migrations.RemoveField(
            model_name='personaje',
            name='titulo_interprete3',
        ),
        migrations.RemoveField(
            model_name='titulo',
            name='imagen2',
        ),
        migrations.RemoveField(
            model_name='titulo',
            name='staff',
        ),
        migrations.DeleteModel(
            name='Staff',
        ),
    ]
