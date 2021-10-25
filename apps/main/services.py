from apps.database.models import Film, Genre

from django.template.defaulttags import register

@register.filter
def get_ip(request, *args, **kwargs):
    # Geting request ip
    return request.META['REMOTE_ADDR']

@register.filter
def get_count_on_stars(value):
    # For rendering count start films average rating
    return range(1, int(value) + 1)
    
@register.filter
def get_count_half_stars(value):
    # For rendering count start films average rating
    return range(int(value) + 1 , int(value) + 2) if value % int(value) else range(0)

@register.filter
def get_count_off_stars(value):
    # For rendering count start films average rating
    if not value:
        return range(1, 11)
        
    if get_count_half_stars(value):
        return range(int(value) + 2, 10 + 1)

    return range(int(value) + 1, 10 + 1)


def get_recommendations_films(count = 5):
    ''' Use **get_recommendations_films() in renders kwargs'''
    return {'recom_films': Film.objects.filter(is_delete = False).order_by('-date_create')[0:count]}

def get_new_films(count = 12):
    ''' Use **get_new_films() in renders kwargs'''
    return {'films': Film.objects.filter(is_delete = False).order_by('-year', '-date_create')[0:count]}

def get_all_genres():
    ''' Use **get_all_genres() in renders kwargs'''
    return {'all_genres': Genre.objects.all()}