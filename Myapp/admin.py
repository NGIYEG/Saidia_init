from django.contrib import admin
from .models import Supporter, Contact, Blogpost
# Register your models here.

admin.site.register(Supporter)
admin.site.register(Contact)
admin.site.register(Blogpost)