# Generated by Django 5.0.4 on 2024-04-16 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_complaintroom_cid'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaintroom',
            name='area',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='complaintroom',
            name='photo',
            field=models.ImageField(default='avatar.svg', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='complaintroom',
            name='subject',
            field=models.CharField(max_length=100),
        ),
    ]