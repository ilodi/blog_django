# Generated by Django 3.1.2 on 2020-10-10 02:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_auto_20201006_2231'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_at'], 'verbose_name': 'Articulo', 'verbose_name_plural': 'Articulos'},
        ),
        migrations.RemoveField(
            model_name='article',
            name='image',
        ),
        migrations.AlterField(
            model_name='article',
            name='categorys',
            field=models.ManyToManyField(blank=True, related_name='articles', to='blog.Category', verbose_name='Categorias'),
        ),
        migrations.AlterField(
            model_name='article',
            name='user',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]