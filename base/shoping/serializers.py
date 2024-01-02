from rest_framework import serializers
from .models import category, product
class productserializer(serializers.ModelSerializers):
    class Meta:
        model=product
        fields=(
            "id",
            "name",
            "get_absolute_url",
            "description",
            "price",
            "get_image",
            "get_thumbnail",
        )
