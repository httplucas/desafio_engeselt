# Generated by Django 5.1.2 on 2024-11-05 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0012_alter_livros_ano_publicacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livros',
            name='quantidade_total',
        ),
        migrations.AlterField(
            model_name='livros',
            name='quantidade_disponivel',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
