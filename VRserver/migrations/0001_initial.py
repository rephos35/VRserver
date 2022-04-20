# Generated by Django 4.0.3 on 2022-04-02 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StatusDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user1', models.TextField()),
                ('user2', models.TextField()),
                ('user3', models.TextField()),
                ('user4', models.TextField()),
                ('user5', models.TextField()),
                ('user6', models.TextField()),
            ],
            options={
                'db_table': 'user_table',
            },
        ),
    ]