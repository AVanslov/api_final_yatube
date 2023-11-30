from django.shortcuts import get_object_or_404
from rest_framework import (
    filters,
    viewsets,
    mixins,
)
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,
)

from posts.models import (
    Comment,
    Group,
    Follow,
    Post,
)

from .permissions import IsOwnerOrReadOnly
from .serializers import (
    CommentSerializer,
    GroupSerializer,
    FollowSerializer,
    PostSerializer,
)


class PostViewSet(viewsets.ModelViewSet):
    """Показывает посты с возможностью редактирования."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Показывает групп постов только для чтения."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly,
    )


class CommentViewSet(viewsets.ModelViewSet):
    """Показывает и редактирует комментарии."""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )

    def get_post(self):
        return get_object_or_404(Post, id=self.kwargs.get('post_id'))

    def get_queryset(self):
        return self.get_post().comments.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post=self.get_post()
        )


# class FollowViewSet(viewsets.ModelViewSet):
class FollowViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """
    Возвращает все подписки пользователя, сделавшего запрос.
    Оформляет подписку от имени пользователя, который сделал запрос,
    на пользователя, переданного в теле запроса.
    """
    serializer_class = FollowSerializer
    permission_classes = (
        IsAuthenticated,
        IsOwnerOrReadOnly,
    )
    filter_backends = (
        filters.SearchFilter,
    )
    search_fields = (
        '=following__username',
    )
    pagination_class = None

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
