# Generated by Django 2.2.7 on 2019-12-16 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='translateword',
            name='word_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='translateword',
            name='word',
            field=models.CharField(db_index=True, max_length=15, verbose_name='Слово'),
        ),
    ]
