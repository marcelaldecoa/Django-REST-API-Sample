from rest_framework import serializers

from . import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""

    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes for our User Profile objects."""

    class Meta:
        model = models.UserProfile
        # Take the fields
        fields = ('id', 'email', 'name', 'password')

        # Arbitrary additional keyword arguments on field
        # Make sure password is write only
        extra_kwargs = {'password': {'write_only': True}}


        def create(self, validated_data):
            """Create and return a new user."""

            user = models.UserProfile(
                email=validated_data['email'],
                name=validated_data['name'],
            )

            # Make sure password is encrypted
            user.set_password(validated_data['password'])

            user.save()

            return user
