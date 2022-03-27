from django.test import TestCase
from django.contrib.auth.models import User


class LogInTest(TestCase):
    def setUp(self):
        self.id = {
            'username': 'jvn',
            'password': 'secret'}
        User.objects.create_user(**self.id)

    def test_login(self):
        response = self.client.post('/login', self.id, follow=True)
        self.assertEqual(response.wsgi_request.user.username, "jvn")
        self.assertEqual(response.status_code, 200)
