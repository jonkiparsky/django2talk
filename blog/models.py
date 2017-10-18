from django.utils import timezone
from django.db.models import (
    CASCADE,
    CharField,
    DateTimeField,
    ForeignKey,
    Model,
    TextField,
)
from django_countries.fields import CountryField

class Post(Model):
    author = ForeignKey('auth.User',
                        CASCADE)
    title = CharField(max_length=200)
    text = TextField()
    created_at = DateTimeField(default=timezone.now)
    published_date = DateTimeField(blank=True,
                                   null=True)
    country = CountryField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
