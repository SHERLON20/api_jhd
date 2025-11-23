from rest_framework import viewsets
from .models import petisco_e_pastel,pedidos,caldo_e_bebidas
from .serializers import petisco_e_pastel_serializer,pedidos_serializer,caldo_e_bebidas_serializer

class petisco_e_pastel_viewset(viewsets.ModelViewSet):
    queryset = petisco_e_pastel.objects.all()
    serializer_class = petisco_e_pastel_serializer

class pedidos_viewset(viewsets.ModelViewSet):
    queryset = pedidos.objects.all()
    serializer_class = pedidos_serializer

class caldo_e_bebidas_viewset(viewsets.ModelViewSet):
    queryset = caldo_e_bebidas.objects.all()
    serializer_class = caldo_e_bebidas_serializer