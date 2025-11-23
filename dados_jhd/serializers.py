from rest_framework import serializers
from .models import petisco_e_pastel,pedidos,caldo_e_bebidas

class petisco_e_pastel_serializer(serializers.ModelSerializer):
    class Meta:
        model = petisco_e_pastel
        fields = ["id","nome","preco","classe"]
class pedidos_serializer(serializers.ModelSerializer):
    class Meta:
        model = pedidos
        fields = ["id","numero_mesa","pedido","visivel","is_delete","total"]

class caldo_e_bebidas_serializer(serializers.ModelSerializer):
    class Meta:
        model = caldo_e_bebidas
        fields = ["id","value","preco","classe"]