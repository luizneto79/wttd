from datetime import datetime

from django.test import TestCase

from eventex.subscriptions.models import Subscription


class TestModelSubscription(TestCase):

    def setUp(self) -> None:
        self.obj = Subscription(name='Luiz Marques Neto', cpf='12345678901',
                           email='luizneto79@gmail.com', phone='51999999999')
        self.obj.save()

    def test_save_subscription(self):

        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)
