from rest_framework import serializers

from .models import Review

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = ('reviewtext', 'sentsum', 'pos', 'neut', 'neg', 'emosum', 'happy', 'angry', 'excited', 'sad', 'bored', 'afraid', 'disgust', 'keyword1', 'keyword2', 'keyword3')
        # fields = ('id', 'Review_name', 'Review_content')
