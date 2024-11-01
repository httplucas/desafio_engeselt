# Generated by Django 5.1.2 on 2024-11-01 02:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Emprestimo',
        ),
        migrations.AlterModelOptions(
            name='livros',
            options={'verbose_name': 'Livros'},
        ),
        migrations.RemoveField(
            model_name='livros',
            name='data_devolucao',
        ),
        migrations.RemoveField(
            model_name='livros',
            name='emprestado',
        ),
        migrations.AlterField(
            model_name='livros',
            name='data_emprestado',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='livros',
            name='descricao',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='livros',
            name='genero',
            field=models.CharField(choices=[('Fic', 'Ficção'), ('Rom', 'Romance'), ('Ter', 'Terror'), ('Aca', 'Ação'), ('Ave', 'Aventura')], max_length=3),
        ),
        migrations.AlterField(
            model_name='livros',
            name='nome_emprestado',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='livros',
            name='tempo_duracao',
            field=models.DateField(blank=True),
        ),
    ]
