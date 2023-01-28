from django.contrib.auth.models import User
from django.test import TestCase

from api.models import Person, Employer


# Create your tests here.
class PersonTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username="admin")
        employer = Employer.objects.create(name="Google")
        Person.objects.create(first_name="John",
                              last_name="Doe",
                              height="157",
                              occupation="Engineer",
                              code="AC!23",
                              owner= user,
                              employer=employer)
        # Person.objects.create(name="cat", sound="meow")

    def test_animals_can_speak(self):
        """Persons that can speak are correctly identified"""
        person = Person.objects.get(first_name="John")
        # cat = Person.objects.get(name="cat")
        self.assertEqual(person.last_name, 'Doe')
