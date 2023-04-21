from rest_framework.serializers import ModelSerializer
from .models import PostIt

class PostItSerializer(ModelSerializer):
    class Meta:
        model = PostIt
        fields = '__all__'