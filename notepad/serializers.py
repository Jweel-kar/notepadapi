from rest_framework import serializers

from .models import Notepad


class NotepadsSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=200, required=True)
    text = serializers.CharField(max_length=1000, required=True)

    def create(self, validated_data):
        # Once the request data has been validated, we can create a title and notes items instance in the database
        return Notepad.objects.create(
            title=validated_data.get('title'),
            text=validated_data.get('text')
        )

    def update(self, instance, validated_data):
        # Once the request data has been validated, we can update the title and notes items instance in the database
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance

    class Meta:
        model = Notepad
        fields = (
            'id',
            'title',
            'text'
        )
