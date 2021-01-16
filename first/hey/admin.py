from django.contrib import admin
from django.conf.urls import url
from django.utils.html import format_html
from django.http import HttpResponseRedirect
from .models import Student, Stage

class StudentAdmin(admin.ModelAdmin): # This is to customize the search and list
        list_display = ('sname','sage','stage', 'custom_column')
        search_fields = ('sname','stage__sstage')
        def custom_column(self, row):
            return format_html('<a href="custom_url?id='+str(row.id)+'">'+'click'+'</a>')

        def custom_url(self, request):
            return HttpResponseRedirect('/admin')

        def get_urls(self):
            urls = super(StudentAdmin, self).get_urls()
            my_urls = [url(r'^custom_url/$', self.custom_url)]
            return my_urls + urls
        #add filters to check the side filter
# Register your models here.


admin.site.register(Student, StudentAdmin)
admin.site.register(Stage)


