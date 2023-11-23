# Generated by Django 4.2.7 on 2023-11-22 23:29

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('home', '0004_teampage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teampage',
            name='member_description',
        ),
        migrations.RemoveField(
            model_name='teampage',
            name='member_image',
        ),
        migrations.RemoveField(
            model_name='teampage',
            name='member_name_surname',
        ),
        migrations.RemoveField(
            model_name='teampage',
            name='member_role',
        ),
        migrations.RemoveField(
            model_name='teampage',
            name='member_socials_fb',
        ),
        migrations.RemoveField(
            model_name='teampage',
            name='member_socials_instagram',
        ),
        migrations.RemoveField(
            model_name='teampage',
            name='member_socials_linkedin',
        ),
        migrations.RemoveField(
            model_name='teampage',
            name='member_socials_x',
        ),
        migrations.RemoveField(
            model_name='teampage',
            name='member_socials_yt',
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('member_name_surname', models.CharField(max_length=81, null=True)),
                ('member_role', models.CharField(max_length=40, null=True)),
                ('member_description', models.CharField(max_length=255, null=True)),
                ('member_socials_fb', models.CharField(max_length=155, null=True)),
                ('member_socials_x', models.CharField(max_length=155, null=True)),
                ('member_socials_instagram', models.CharField(max_length=155, null=True)),
                ('member_socials_linkedin', models.CharField(max_length=155, null=True)),
                ('member_socials_yt', models.CharField(max_length=155, null=True)),
                ('member_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_members', to='home.teampage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]