from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from core_apps.common.models import TimeStampedUUIDModel


User = get_user_model()

class Comment(TimeStampedUUIDModel):
    article = models.ForeignKey("articles.Article", on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey("profiles.Profile", on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return f"{self.author} commented on {self.article}"