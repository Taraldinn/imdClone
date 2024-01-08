from rest_framework import serializers

from watchlist.models import Review, WatchList, StreamPlatform


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=200)
#     description = serializers.CharField(max_length=300)
#     active = serializers.BooleanField(default=True)
#
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get(
#             'description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)    
    class Meta:
        model = Review
        # fields = '__all__'
        exclude = ['watchlist']




class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = WatchList
        fields = '__all__'
        # exclude = ['active']


class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    watch = WatchListSerializer(many=True)
    class Meta:
        model = StreamPlatform
        fields = '__all__'

        
