from django.conf import settings
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from drf_yasg.utils import swagger_auto_schema
from .serializers_notify import NotifySerializer, STATUS_ENUM, CHANNEL_ENUM
from .serializers_response import ResponseSerializer
from rest_framework.permissions import IsAuthenticated



class SendMessageToSlack(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(operation_description="Notify liveroom broadcast and error msg to Slack", request_body=NotifySerializer,  responses={200: ResponseSerializer})
    def get(self, request):
        return Response({"message": "Hello, World!", "env" : settings.SUPER_ACCOUNT_ACCOUNT}, status=status.HTTP_200_OK)
        # return Response({"message": "Hello, World!", "env" : f"{settings.SUPER_ACCOUNT_ACCOUNT}"}, status=status.HTTP_200_OK)
    # def post(self, request, *args, **kwargs):
    #     serializer = NotifySerializer(data=request.data)
    #     if serializer.is_valid():
    #         data = serializer.validated_data
    #          # Valid data; process it as needed
    #         # return Response(serializer.validated_data, status=status.HTTP_200_OK)
    #         webhook_url = 'https://hooks.slack.com/services/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'
    #         # Replace with your actual webhook URL
    #         status_key = serializer.validated_data['status']
    #         status = STATUS_ENUM[status_key].value
    #         channel_key = serializer.validated_data['channel']
    #         channel = CHANNEL_ENUM[channel_key].value
    #         message = serializer.validated_data.get('message', None)
    #         if  message is not None:
    #             message = f"{status} - {data['message']}"
    #         else:
    #             message = status
    #         # notify_message = f"【{data['channel']}】{data['name']}：{message} \n URL: {data['url']}"
    #         icon = ':white_check_mark:'
    #         if status_key == 'error':
    #             icon = ':x:'
    #         slack_data = {"blocks": [
    #                 {
    #                     "type": "header",
    #                     "text": {
    #                         "type": "plain_text",
    #                         "text": "直播主控台通知：",
    #                         "emoji": True
    #                     }
    #                 },
    #                 {
    #                     "type": "section",
    #                     "block_id": "section-liveroom-notify",
    #                     "text": {
    #                         "type": "mrkdwn",
    #                         "text": f"<{data['live_url']}|【{channel}】{data['name']}> {icon} \n {message}"
    #                     },
    #                 },
    #                 {
    #                     "type": "section",
    #                     "text": {
    #                         "type": "mrkdwn",
    #                         "text": "前往直播主控台"
    #                     },
    #                     "accessory": {
    #                         "type": "button",
    #                         "text": {
    #                             "type": "plain_text",
    #                             "text": "前往",
    #                             "emoji": True
    #                         },
    #                         "value": "go_to_liveroom",
    #                         "url": f"{data['liveroom_url']}",
    #                         "action_id": "button-action"
    #                     }
    #                 }
    #             ]}
    #         response = requests.post(
    #             webhook_url, json=slack_data,
    #             headers={'Content-Type': 'application/json'}
    #         )
    #         if response.status_code != 200:
    #             return Response({'message': f"{response.text}", 'code': f"{response.status_code}"}, status=500)
    #         return Response({'message': 'success', "code": 0}, status=200)
    #     else:
    #         # Invalid data; return an error response
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     