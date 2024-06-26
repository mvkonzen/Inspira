# Generated by Django 4.1.7 on 2023-02-16 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('cod_assessor', models.CharField(max_length=50)),
                ('negocio', models.CharField(max_length=100)),
                ('cliente', models.CharField(max_length=15)),
                ('data_inicial', models.CharField(max_length=100)),
                ('data_final', models.CharField(max_length=50)),
                ('empresa_parceira', models.CharField(max_length=50)),
                ('anotacoes', models.CharField(max_length=20)),
            ],
        ),
    ]
