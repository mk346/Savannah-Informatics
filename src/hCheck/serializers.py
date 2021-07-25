from .models import healthSys
from rest_framework import serializers

class mySerializer(serializers.ModelSerializer):
	class Meta:
		model = healthSys
		fields = '__all__'
