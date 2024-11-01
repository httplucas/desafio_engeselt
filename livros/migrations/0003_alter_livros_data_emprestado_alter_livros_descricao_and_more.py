# Generated by Django 5.1.2 on 2024-11-01 02:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0002_delete_emprestimo_alter_livros_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='data_emprestado',
            field=models.DateField(default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name='livros',
            name='descricao',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='livros',
            name='genero',
            field=models.CharField(blank=True, choices=[('Fic', 'Ficção'), ('Rom', 'Romance'), ('Ter', 'Terror'), ('Aca', 'Ação'), ('Ave', 'Aventura')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='livros',
            name='nome_emprestado',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='livros',
            name='tempo_duracao',
            field=models.DateField(blank=True, null=True),
        ),
    ]
