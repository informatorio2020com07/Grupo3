# Generated by Django 3.1.1 on 2020-10-02 16:50

from django.db import migrations, models
import myapps.categorias.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('foto', models.ImageField(blank=True, default='img/categorias/img_defecto/categoria-img.jpg', null=True, upload_to=myapps.categorias.models.get_image_path)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
