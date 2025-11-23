from django.contrib import admin
from .models import petisco_e_pastel,pedidos,caldo_e_bebidas

class lanches_e_pasteis(admin.ModelAdmin):
    list_display = ("id","nome","preco","classe")
    list_display_links = ("id","nome")
    list_per_page = 20
    search_fields = ("nome","classe")
admin.site.register(petisco_e_pastel,lanches_e_pasteis)

class lista_pedidos(admin.ModelAdmin):
    list_display =("id","numero_mesa","pedido","visivel","is_delete","total")
    list_display_links =("id","numero_mesa")
    list_per_page = 20
    search_fields = ("id","numero_mesa")
admin.site.register(pedidos,lista_pedidos)

class porcoes_e_bebidas(admin.ModelAdmin):
    list_display =("id","value","preco","classe")
    list_display_links=("id","value")
    list_per_page = 20
    search_fields = ("value","classe")
admin.site.register(caldo_e_bebidas,porcoes_e_bebidas)
