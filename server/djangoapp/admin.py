from django.contrib import admin
# from .models import related models
from .models import CarMake
from .models import CarModel

# Register your models here.

# CarModelInline class
# admin.site.register(CarModelInline)
# CarModelAdmin class
# admin.site.register(CarModelAdmin)
# CarMakeAdmin class with CarModelInline
#admin.site.register(CarMakeAdmin, CarModelInline)
# Register models here
admin.site.register(CarMake)
admin.site.register(CarModel)