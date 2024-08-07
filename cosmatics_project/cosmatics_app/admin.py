from django.contrib import admin
from cosmatics_app.models import User , Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'image', 'created_at', 'updated_at')

admin.site.register(User)

admin.site.register(Product)
