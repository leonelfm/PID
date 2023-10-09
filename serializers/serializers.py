from rest_framework import serializers


class OrderSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    item = serializers.CharField()
    quantity = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2, min_value=0)
    status = serializers.ChoiceField(choices=["completed", "pending", "canceled"])


class SolutionSerializer(serializers.Serializer):
    orders = OrderSerializer(many=True)
    criterion = serializers.CharField()
