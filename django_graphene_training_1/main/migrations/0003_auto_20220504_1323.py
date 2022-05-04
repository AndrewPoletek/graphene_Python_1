# Generated by Django 3.2.13 on 2022-05-04 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_book_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoverColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(choices=[('BLACK', 'BLACK'), ('RED', 'RED'), ('YELLOW', 'YELLOW')], max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='main.author'),
        ),
    ]
