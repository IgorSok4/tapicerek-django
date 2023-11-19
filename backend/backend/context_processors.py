from home.models import HomePage

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