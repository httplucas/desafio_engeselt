# Generated by Django 5.1.2 on 2024-11-05 19:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0015_remove_livros_data_emprestado_and_more'),
        ('usuarios', '0004_alter_usuario_endereco_alter_usuario_telefone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='livro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='livros.livros'),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='nome_emprestado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.usuario'),
            preserve_default=False,
        ),
    ]
