# Generated by Django 3.2.7 on 2021-11-08 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postImage',
            field=models.ImageField(blank=True, null=True, upload_to='Post/media'),
        ),
    ]