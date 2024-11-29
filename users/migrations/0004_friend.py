# Generated by Django 5.1.3 on 2024-11-29 12:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accepted_time_1', models.DateTimeField(blank=True, null=True)),
                ('accepted_time_2', models.DateTimeField(blank=True, null=True)),
                ('user_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friendships_as_user_1', to=settings.AUTH_USER_MODEL)),
                ('user_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friendships_as_user_2', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'constraints': [models.UniqueConstraint(fields=('user_1', 'user_2'), name='unique_friendship')],
            },
        ),
    ]