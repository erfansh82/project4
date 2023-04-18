from rest_framework import serializers

from .models import ActivePlan,CreatePlan


class CreatePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model=CreatePlan
        fields='__all__'


class ActivePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model=ActivePlan
        fields='__all__'

        