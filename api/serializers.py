from rest_framework import serializers


class RequestSerializer(serializers.Serializer):
    # expectedKeys = ['operation', 'color', 'representation', 'amount']
    # expectedKeys = ['color', 'representation', 'conversion']
    representation = serializers.CharField(required=True)
    try:
        color = serializers.ListField()
    except serializers.ValidationError:
        color = serializers.CharField()
