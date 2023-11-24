from home.models import (
    HomePage,
    TeamPage,
    ServicesPage,
)
from contact.models import ContactPage

def global_homepage_data(request):
    home_page = HomePage.objects.first()
    if home_page:
        return {
            'logo_image': home_page.logo_image,
            'logo_image_2': home_page.logo_image_2,

            'street': home_page.street,
            'zip_city': home_page.zip_city,
            'tel_home': home_page.tel_home,
            'tel_mobi': home_page.tel_mobi,
            'email': home_page.email,

            'open_mon': home_page.open_mon,
            'open_tue': home_page.open_tue,
            'open_wed': home_page.open_wed,
            'open_thu': home_page.open_thu,
            'open_fri': home_page.open_fri,
            'open_sat': home_page.open_sat,
            'open_sun': home_page.open_sun,
        }
    return {}

def global_page_links(request):
    return {
        'contact_page': ContactPage.objects.live().first(),
        'team_page': TeamPage.objects.live().first(),
        'service_page': ServicesPage.objects.live().first(),
    }
