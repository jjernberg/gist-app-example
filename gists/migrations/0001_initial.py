# Generated by Django 3.2.4 on 2021-06-02 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteGist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gist_id', models.CharField(max_length=30)),
                ('git_username', models.CharField(max_length=120)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteGistFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gist_id', models.CharField(max_length=30)),
                ('file_key', models.CharField(max_length=512)),
            ],
        ),
    ]
