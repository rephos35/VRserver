from VRserver.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # serializer_choice_field = ('user1', 'user2', 'user3', 'user4', 'user5', 'user6')
