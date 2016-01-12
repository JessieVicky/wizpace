import os

def populate():
    Site.objects.get_or_create(pk=2, domain='wizpace.com', name='Wizpace')
    Group.objects.get_or_create(pk=1, name='Clients')
    Group.objects.get_or_create(pk=2, name='Freelancers')


if __name__ == '__main__':
    print "Executing population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wizpace.settings')
    from django.contrib.sites.models import Site
    from django.contrib.auth.models import Group

    import django
    django.setup()

    populate()
    print "Population script done!"