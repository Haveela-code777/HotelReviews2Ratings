# Generated by Django 4.0.2 on 2022-03-31 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hotelapp', '0003_alter_hotel_number_of_reviews_alter_hotel_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('rating', models.FloatField(default=0)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelapp.hotel')),
            ],
        ),
    ]
