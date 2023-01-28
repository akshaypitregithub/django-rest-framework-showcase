from django.db import models

GERMAN = 'DE'
FRENCH = 'FR'
ENGLISH = 'EN'
LANGUAGE_CHOICES = [
    (GERMAN, 'German'),
    (FRENCH, 'French'),
    (ENGLISH, 'English')
]


class Employer(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    height = models.CharField(max_length=200)
    occupation = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    employed = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='ENGLISH', max_length=100)
    employer = models.ForeignKey(to=Employer, on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
