from enum import Enum

class STATUS_ENUM(Enum):
    live = '開播'
    error = '異常'
    # Define other statuses as needed
    
class CHANNEL_ENUM(Enum):
    page = 'Facebook粉絲專頁'
    group = 'Facebook社團'
    instagram = 'Instagram'
    # Define other statuses as needed

from rest_framework import serializers

class NotifySerializer(serializers.Serializer):
    status = serializers.ChoiceField(choices=[(e.name, e.value) for e in STATUS_ENUM])
    name = serializers.CharField()
    message = serializers.CharField(required=False, allow_blank=True)
    channel = serializers.ChoiceField(choices=[(e.name, e.value) for e in CHANNEL_ENUM])
    live_url = serializers.URLField()
    liveroom_url = serializers.URLField()