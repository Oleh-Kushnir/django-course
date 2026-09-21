from rest_framework import serializers
from rest_framework import fields

from products.models import Products, ProductCategory, Basket


class ProductsSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Products
        fields = ('id', 'name', 'price', 'description', 'category', 'quantity', 'image')


class BasketSerializer(serializers.ModelSerializer):
    product = ProductsSerializer()
    sum = fields.FloatField(read_only=False)
    total_sum = fields.SerializerMethodField()
    total_quantity = fields.SerializerMethodField()

    class Meta:
        model = Basket
        fields = ('id', 'product', 'quantity', 'sum', 'total_quantity', 'created_timestamp')
        read_only_fields = ('created_timestamp',)

    def get_total_sum(self, obj):
        return Basket.objects.filter(user_id=obj.user.id).total_sum()

    def get_total_quantity(self, obj):
        return Basket.objects.filter(user_id=obj.user.id).total_quantity()
