# Generated by Django 3.1.4 on 2021-01-24 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('klasses', '0001_initial'),
        ('people', '0001_initial'),
        ('courses', '0002_auto_20210124_1041'),
        ('curriculum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentstudysubject',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='people.studentprofile'),
        ),
        migrations.AddField(
            model_name='studentstudysubject',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='curriculum.subject'),
        ),
        migrations.AddField(
            model_name='klassstudiedsubject',
            name='courses',
            field=models.ManyToManyField(related_name='subject', through='curriculum.AddCourseToSubject', to='courses.Course'),
        ),
        migrations.AddField(
            model_name='klassstudiedsubject',
            name='klass',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='klasses.studentclass'),
        ),
        migrations.AddField(
            model_name='klassstudiedsubject',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='curriculum.subject'),
        ),
        migrations.AddField(
            model_name='klassstudiedsubject',
            name='subject_teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='taught_subjects', to='people.teacherprofile'),
        ),
        migrations.AddField(
            model_name='addcoursetosubject',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courses.course'),
        ),
        migrations.AddField(
            model_name='addcoursetosubject',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='curriculum.klassstudiedsubject'),
        ),
        migrations.AlterUniqueTogether(
            name='studentstudysubject',
            unique_together={('student', 'subject')},
        ),
        migrations.AlterUniqueTogether(
            name='klassstudiedsubject',
            unique_together={('klass', 'subject')},
        ),
        migrations.AlterUniqueTogether(
            name='addcoursetosubject',
            unique_together={('course', 'subject')},
        ),
    ]
