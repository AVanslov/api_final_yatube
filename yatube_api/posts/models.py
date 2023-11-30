from django.contrib.auth import get_user_model
from django.db import models


MAXIMUM_STRING_LENGTH = 256

NUMBER_OF_VISIBLE_CHARACTERS = 15

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=MAXIMUM_STRING_LENGTH)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return (
            self.title[:NUMBER_OF_VISIBLE_CHARACTERS],
            self.slug[:NUMBER_OF_VISIBLE_CHARACTERS],
            self.description[:NUMBER_OF_VISIBLE_CHARACTERS],
        )


class Post(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
    )
    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
    )
    image = models.ImageField(
        upload_to='posts/',
        null=True,
        blank=True,
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='posts',
        blank=True,
        null=True,
    )

    def __str__(self):
        return (
            self.author[:NUMBER_OF_VISIBLE_CHARACTERS],
            self.title[:NUMBER_OF_VISIBLE_CHARACTERS],
            self.text[:NUMBER_OF_VISIBLE_CHARACTERS],
            self.pub_date[:NUMBER_OF_VISIBLE_CHARACTERS],
            self.image[:NUMBER_OF_VISIBLE_CHARACTERS],
            self.group[:NUMBER_OF_VISIBLE_CHARACTERS],
        )


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True,
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
    )

    def __str__(self):
        return (
            self.author[:NUMBER_OF_VISIBLE_CHARACTERS],
            self.text[:NUMBER_OF_VISIBLE_CHARACTERS],
            self.created[:NUMBER_OF_VISIBLE_CHARACTERS],
            self.post[:NUMBER_OF_VISIBLE_CHARACTERS],
        )


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
    )
