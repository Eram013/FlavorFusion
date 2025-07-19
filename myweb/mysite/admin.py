from django.contrib import admin
from .models import user

class userAdmin(admin.ModelAdmin):
    list_display=('name','price','quantity')
admin.site.register(user,userAdmin)