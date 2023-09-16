from django.contrib import admin
from home.models import Contact , Lectures , Booking

# Register your models here.
admin.site.register(Contact)

class Lecutrestable(admin.ModelAdmin):
    list_display = ['Lecture_ID' , 'Faculty_Name' , 'Subject' , 'Date' , 'Time']
    search_fields = ['Subject']
    list_per_page = 10


admin.site.register(Lectures)

class select(admin.ModelAdmin):
    list_display = ['date' , 'time' , 'lecture' , 'name' , 'email ', 'phone' , 'college' , 'branch' ]
    search_fields = ['name']
    list_per_page = 10
    

admin.site.register(Booking)