# Generated by Django 2.0.2 on 2018-02-13 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coursesapp', '0005_auto_20180213_1203'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['name'], 'verbose_name': 'Curso', 'verbose_name_plural': 'Cursos'},
        ),
        migrations.RenameField(
            model_name='course',
            old_name='crated_at',
            new_name='created_at',
        ),
    ]