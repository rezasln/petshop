from rest_framework import serializers
from .models import Product, Collection

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title','unit_price', 'inventory','collection']
        read_only_fields = ['id']

    collection = serializers.PrimaryKeyRelatedField(queryset=Collection.objects.all())

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']
        read_only_fields = ['id']

    products_count = serializers.IntegerField()

    