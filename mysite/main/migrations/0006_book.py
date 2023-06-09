# Generated by Django 4.2.1 on 2023-05-24 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_delete_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Book name')),
                ('about', models.TextField(verbose_name='Book about')),
                ('price', models.PositiveIntegerField(verbose_name='Book price')),
                ('date', models.DateTimeField(auto_now=True)),
                ('img', models.ImageField(upload_to='books', verbose_name='Book image')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_author', to='main.author')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
