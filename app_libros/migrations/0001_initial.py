# Generated by Django 3.1.5 on 2021-03-19 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('le_gusta', models.ManyToManyField(null=True, related_name='libro_favorito', to='login_app.Usuario')),
                ('subido_por_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='libro_subido', to='login_app.usuario')),
            ],
        ),
    ]
