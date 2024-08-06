from django.contrib import admin
from .models import Loja, Carros, Vendas
# Register your models here.

admin.site.register(Loja)
admin.site.register(Carros)
admin.site.register(Vendas)