# Generated by Django 2.0.2 on 2018-02-13 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursesapp', '0007_auto_20180213_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='about',
            field=models.TextField(blank=True, verbose_name='Sobre o curso'),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(blank=True, verbose_name='Descrição Simples'),
        ),
    ]