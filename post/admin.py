from django.contrib import admin
from .models import article,Category,Comment,contact_us
admin.site.register(article)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(contact_us)


