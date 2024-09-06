from rest_framework import serializers

class ResponseSerializer(serializers.Serializer):
    code = serializers.IntegerField()
    message = serializers.CharField(required=False, allow_blank=True)