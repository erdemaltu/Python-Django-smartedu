# Generated by Django 4.2.2 on 2023-07-09 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='courses.tag'),
        ),
    ]