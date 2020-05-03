# Generated by Django 2.2.6 on 2020-05-03 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='time',
            field=models.CharField(choices=[('0', 'Thứ 2'), ('1', 'Thứ 3'), ('2', 'Thứ 4'), ('3', 'Thứ 5'), ('4', 'Thứ 6'), ('5', 'Thứ 7')], default='-----', max_length=20),
        ),
        migrations.AlterField(
            model_name='class',
            name='grade',
            field=models.CharField(choices=[('0', '10'), ('1', '11'), ('2', '12')], default='-----', max_length=20),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='semester',
            field=models.CharField(choices=[('0', '1'), ('1', '2')], default='-----', max_length=20, verbose_name='Học kỳ'),
        ),
        migrations.AlterField(
            model_name='score',
            name='type',
            field=models.CharField(choices=[('0', "Điểm 15'"), ('1', "Điểm 45'"), ('2', "Điểm học kỳ'"), ('3', "Điểm miệng'")], default='-----', max_length=20),
        ),
    ]
