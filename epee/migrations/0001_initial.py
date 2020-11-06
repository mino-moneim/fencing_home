# Generated by Django 3.1.3 on 2020-11-06 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Epee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('weapon_name', models.CharField(max_length=50)),
                ('size', models.CharField(choices=[('normal', 'normal'), ('mini', 'mini')], max_length=50)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
    ]
