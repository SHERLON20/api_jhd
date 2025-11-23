from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from dados_jhd.views import petisco_e_pastel_viewset,pedidos_viewset,caldo_e_bebidas_viewset

router = routers.DefaultRouter()
router.register("petisco_e_pastel",petisco_e_pastel_viewset,basename="lanche_e_pastel")
router.register("pedidos",pedidos_viewset,basename="pedidos")
router.register("caldo_e_bebidas",caldo_e_bebidas_viewset,basename="porcao_e_bebidas")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]