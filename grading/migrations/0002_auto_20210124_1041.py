# Generated by Django 3.1.4 on 2021-01-24 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('people', '0001_initial'),
        ('courses', '0002_auto_20210124_1041'),
        ('klasses', '0001_initial'),
        ('grading', '0001_initial'),
        ('curriculum', '0002_auto_20210124_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='grades', to='people.student'),
        ),
        migrations.AddField(
            model_name='graderecord',
            name='grade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='grade_records', to='grading.coursegrade'),
        ),
        migrations.AddField(
            model_name='graderecord',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course_grades', to='people.studentprofile'),
        ),
        migrations.AddField(
            model_name='generalgrade',
            name='klass',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ongoing_grades', to='klasses.studentclass'),
        ),
        migrations.AddField(
            model_name='generalgrade',
            name='recorded_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='marklist', to='people.teacherprofile'),
        ),
        migrations.AddField(
            model_name='generalgrade',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='curriculum.subject'),
        ),
        migrations.AddField(
            model_name='coursegrade',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='grades', to='courses.course'),
        ),
        migrations.AddField(
            model_name='coursegrade',
            name='klass',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ongoing_course_grades', to='klasses.studentclass'),
        ),
    ]
