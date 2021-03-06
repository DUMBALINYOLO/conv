# Generated by Django 3.1.4 on 2021-01-24 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('curriculum', '0002_auto_20210124_1041'),
        ('people', '0001_initial'),
        ('klasses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentclass',
            name='class_teacher',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='people.teacherprofile'),
        ),
        migrations.AddField(
            model_name='studentclass',
            name='stream',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='classes', to='klasses.stream'),
        ),
        migrations.AddField(
            model_name='studentclass',
            name='subjects',
            field=models.ManyToManyField(through='curriculum.KlassStudiedSubject', to='curriculum.Subject'),
        ),
    ]
