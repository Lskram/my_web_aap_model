# Generated by Django 4.2.2 on 2023-08-03 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebGame', '0002_alter_student_options_student_prefix'),
    ]

    operations = [
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Major',
                'verbose_name_plural': 'Majors',
            },
        ),
    ]
