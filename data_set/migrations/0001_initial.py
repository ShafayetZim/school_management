# Generated by Django 4.1.7 on 2023-03-10 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=250)),
                ('dob', models.DateField(blank=True, null=True)),
                ('user_type', models.IntegerField(default=2)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_set.class')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_code', models.CharField(blank=True, max_length=250, null=True)),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('contact', models.CharField(blank=True, max_length=250, null=True)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_set.class')),
            ],
        ),
        migrations.CreateModel(
            name='ClassStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classIns', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_set.activeclass')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_set.student')),
            ],
        ),
        migrations.AddField(
            model_name='activeclass',
            name='assigend_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_set.class'),
        ),
        migrations.AddField(
            model_name='activeclass',
            name='assigend_subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_set.subject'),
        ),
        migrations.AddField(
            model_name='activeclass',
            name='assigned_teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_set.teacher'),
        ),
    ]
