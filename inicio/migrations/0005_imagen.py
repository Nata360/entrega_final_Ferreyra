# Generated by Django 4.2.3 on 2023-07-20 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0004_remove_albunimagen_albun_delete_albun_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='galeria/imagenes')),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.TextField(max_length=500, null=True)),
            ],
        ),
    ]