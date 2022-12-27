from rest_framework import serializers
from .models import STUDENT


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model=STUDENT
        fields="__all__"

