# Generated by Django 3.1.1 on 2020-10-02 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Título')),
                ('content', models.TextField(verbose_name='Contenido')),
                ('slug', models.CharField(max_length=144, unique=True, verbose_name='URL amigable')),
                ('visible', models.BooleanField(verbose_name='¿Visble?')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Crado el')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
            ],
            options={
                'verbose_name': 'Página',
                'verbose_name_plural': 'Páginas',
            },
        ),
    ]
