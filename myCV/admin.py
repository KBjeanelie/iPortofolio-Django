from django.contrib import admin

# Register your models here.
from myCV.models import Skills, Category, Portfolio, Education, Testimonials, Profile

admin.site.register(Skills)
admin.site.register(Category)
admin.site.register(Portfolio)
admin.site.register(Education)
admin.site.register(Testimonials)
admin.site.register(Profile)

