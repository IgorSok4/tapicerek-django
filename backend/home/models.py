from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.search import index


class HomePage(Page):
    templates = 'home/index.html'


    # DATABASE FIELDS

    # logo image
    logo_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    #logo on the right side of nav
    logo_image_2 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # main images on the top of the website
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    main_image_1 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    main_image_2 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # out projects
    title_project_1 = models.CharField(max_length=56, null=True)
    description_project_1 = models.CharField(max_length=254, null=True)
    main_project_1 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    title_project_2 = models.CharField(max_length=56, null=True)
    description_project_2 = models.CharField(max_length=254, null=True)
    main_project_2 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    title_project_3 = models.CharField(max_length=56, null=True)
    description_project_3 = models.CharField(max_length=254, null=True)
    main_project_3 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # about company, what we do, etc.
    title_1 = models.CharField(max_length=56, null=True)
    body_1 = RichTextField(null=True)
    title_2 = models.CharField(max_length=56, null=True)
    body_2 = RichTextField(null=True)

    # footer

    #hours
    open_mon = models.CharField(max_length=14, null=True)
    open_tue = models.CharField(max_length=14, null=True)
    open_wed = models.CharField(max_length=14, null=True)
    open_thu = models.CharField(max_length=14, null=True)
    open_fri = models.CharField(max_length=14, null=True)
    open_sat = models.CharField(max_length=14, null=True)
    open_sun = models.CharField(max_length=14, null=True)

    #contact
    street = models.CharField(max_length=100, null=True)
    zip_city = models.CharField(max_length=100, null=True)
    tel_home = models.CharField(max_length=15, null=True)
    tel_mobi = models.CharField(max_length=15, null=True)
    email = models.EmailField(max_length=254, null=True)


    content_panels = Page.content_panels + [
        FieldPanel('logo_image'),
        FieldPanel('logo_image_2'),
        FieldPanel('main_image'),
        FieldPanel('main_image_1'),
        FieldPanel('main_image_2'),
        MultiFieldPanel([
            FieldPanel('title_project_1'),
            FieldPanel('description_project_1'),
            FieldPanel('main_project_1'),
        ], heading="Projekt 1"),
        MultiFieldPanel([
            FieldPanel('title_project_2'),
            FieldPanel('description_project_2'),
            FieldPanel('main_project_2'),
        ], heading="Projekt 2"),
        MultiFieldPanel([
            FieldPanel('title_project_3'),
            FieldPanel('description_project_3'),
            FieldPanel('main_project_3'),
        ], heading="Projekt 3"),
        MultiFieldPanel([
            FieldPanel('title_1'),
            FieldPanel('body_1'),
            FieldPanel('title_2'),
            FieldPanel('body_2'),
        ], heading="O firmie"),
        MultiFieldPanel([
            FieldPanel('open_mon'),
            FieldPanel('open_tue'),
            FieldPanel('open_wed'),
            FieldPanel('open_thu'),
            FieldPanel('open_fri'),
            FieldPanel('open_sat'),
            FieldPanel('open_sun'),
        ], heading="Godziny otwarcia"),
        MultiFieldPanel([
            FieldPanel('street'),
            FieldPanel('zip_city'),
            FieldPanel('tel_home'),
            FieldPanel('tel_mobi'),
            FieldPanel('email'),
        ], heading="Kontakt"),
    ]


# Models for Team Page ~ Zakładka zespół
class TeamMember(Orderable):
    page = ParentalKey('TeamPage', related_name='team_members')
    member_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    member_name_surname = models.CharField(max_length=81, null=True)
    member_role = models.CharField(max_length=40, null=True)
    member_description = models.CharField(max_length=255, null=True)

    # socials
    member_socials_fb = models.CharField(max_length=155, null=True,
                                         blank=True)
    member_socials_x = models.CharField(max_length=155, null=True,
                                        blank=True)
    member_socials_instagram = models.CharField(max_length=155, null=True,
                                                blank=True)
    member_socials_linkedin = models.CharField(max_length=155, null=True,
                                               blank=True)
    member_socials_yt = models.CharField(max_length=155, null=True,
                                         blank=True)

    panels = [
        FieldPanel('member_image'),
        FieldPanel('member_name_surname'),
        FieldPanel('member_role'),
        FieldPanel('member_description'),
        MultiFieldPanel([
            FieldPanel('member_socials_fb'),
            FieldPanel('member_socials_x'),
            FieldPanel('member_socials_instagram'),
            FieldPanel('member_socials_linkedin'),
            FieldPanel('member_socials_yt'),
        ], heading="Social Media Links")
    ]


class TeamPage(Page):
    content_panels = Page.content_panels + [
    InlinePanel('team_members', label="Team Members"),
    ]