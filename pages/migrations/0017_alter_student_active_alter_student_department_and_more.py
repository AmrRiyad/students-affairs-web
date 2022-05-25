# Generated by Django 4.0.4 on 2022-05-25 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_alter_student_active_alter_student_department_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='active',
            field=models.CharField(choices=[('1', 'Active'), ('0', 'Inactive')], max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.CharField(choices=[('0', 'General'), ('1', 'AI'), ('2', 'CS'), ('3', 'IS'), ('4', 'IT'), ('5', 'DS')], max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.CharField(choices=[('1', 'Male'), ('0', 'Female')], max_length=10),
        ),
    ]