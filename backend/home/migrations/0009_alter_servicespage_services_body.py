# Generated by Django 4.2.7 on 2023-11-23 17:30

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_servicespage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicespage',
            name='services_body',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock(form_classname='full title')), ('paragraph', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('alert', wagtail.blocks.CharBlock(form_classname='alert'))], use_json_field=True),
        ),
    ]