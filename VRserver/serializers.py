from VRserver.models import StatusDB
from rest_framework import serializers


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusDB
        fields = '__all__'
        # serializer_choice_field = ('user1', 'user2', 'user3', 'user4', 'user5', 'user6')
