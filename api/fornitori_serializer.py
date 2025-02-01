from rest_framework import serializers

from home.models import Fornitori


class Fornitoriserializer(serializers.ModelSerializer):

    class Meta:
        model = Fornitori

        fields = '__all__'