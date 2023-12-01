from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator


from posts.models import (
    Comment,
    Follow,
    Group,
    Post,
    User,
)


class PostSerializer(serializers.ModelSerializer):
    """
    Показывает список всех публикаций.
    При указании параметров limit и offset
    показывет все публикации с пагинацией.
    Показывает отдельную публикацию и
    позволяет редактировать или удалять публикацию её автору.
    Добавляет новую публикацию в коллекцию пользователя,
    который сделал запрос.
    """

    author = SlugRelatedField(
        slug_field='username',
        read_only=True,
    )

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    """
    Показывает все комментарии публикации.
    Показывает конкретный комментарий.
    Добавляет новый комментарий от имени
    авторизованного пользователя.
    Позволяет редактировать или удалять комментарий её автору.
    """

    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):
    """
    Показывает список всех доступных сообществ.
    Показывает информацию о конкретном сообществе.
    """

    class Meta:
        model = Group
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    """
    Показывает список всех подписок пользователя,
    который сделал запрос.
    Оформляет подписку от имени пользователя,
    который сделал запрос, на пользователя,
    который передан в теле запроса.
    Запросы разрешены только
    авторизированным пользователям.
    """

    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault(),
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
    )

    class Meta:
        model = Follow
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
                message='Вы уже подписаны на этого автора',
            )
        ]

    def validate_following(self, data):
        request = self.context.get('request')
        if request.user == data:
            raise serializers.ValidationError(
                'Вы не можете подписаться на себя.'
            )
        return data
