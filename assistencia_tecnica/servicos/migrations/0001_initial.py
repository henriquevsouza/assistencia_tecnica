# Generated by Django 4.1.3 on 2022-12-07 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0002_alter_computador_computador_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaManutencao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(choices=[('FCB', 'Formatação com Backup'), ('FSB', 'Formatação sem Backup'), ('MDC', 'Montagem de Desktop Completa'), ('MNC', 'Montagem de Notebook Completa'), ('LC', 'Limpeza Completa')], max_length=5)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('data_inicio', models.DateField(null=True)),
                ('data_entrega', models.DateField(null=True)),
                ('finalizado', models.BooleanField(default=False)),
                ('protocolo', models.CharField(blank=True, max_length=52, null=True)),
                ('categoria_manutencao', models.ManyToManyField(to='servicos.categoriamanutencao')),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clientes.cliente')),
            ],
        ),
    ]
