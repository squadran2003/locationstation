from rest_framework import serializers

class OutCodeSerializer(serializers.Serializer):
    listing_count = serializers.IntegerField(default=1,source='price__count')
    average_daily_price = serializers.IntegerField(default=1,source='price__avg')


class OutCodesSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=10)
    listing_count = serializers.IntegerField(default=1,source='price__count')
    average_daily_price = serializers.IntegerField(default=1,source='price__avg')
    distance = serializers.DecimalField(default=-1.0,max_digits=5,decimal_places=1)

class NexusSerializer(serializers.Serializer):
    nexus_outcode = serializers.CharField(max_length=10)
    listing_count = serializers.IntegerField(default=1,source='price__count')
    average_daily_price = serializers.IntegerField(default=1,source='price__avg')
    outcodes = OutCodesSerializer(many=True)