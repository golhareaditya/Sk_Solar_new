from django.contrib import admin
from .models import Contact, Feedback, Quote

admin.site.site_header = "Administration"
admin.site.site_title = "Administration"
admin.site.index_title = "Administration Panel"
admin.site.register(Quote)
admin.site.register(Contact)
admin.site.register(Feedback)
