# Generated by Django 5.0.3 on 2024-03-27 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='lista_clientes',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(default='Nome Padrão', max_length=255)),
                ('idade', models.IntegerField()),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fotos_clientes')),
            ],
        ),
    ]
