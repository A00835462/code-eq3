from rest_framework import serializers
from tc2005.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):

    total_score = serializers.CharField()
    average_score = serializers.CharField()
    
    class Meta:
        model = User
        fields = "__all__"
        # extra_kwargs = {
        #     "password": {
        #         "write_only":True,
        #         "style":{"input_type":"password"}
        #     }
        # }

class LoginSerializer(serializers.Serializer):
    password = serializers.CharField(

        required=True,
        style={'input_type': 'password'}
    )
    email = serializers.CharField(

        required=True,
      
    )
        