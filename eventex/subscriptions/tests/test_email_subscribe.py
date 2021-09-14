from django.test import TestCase

from django.core import mail


class SubscribePostValid(TestCase):

    def setUp(self):
        data = dict(name='Luiz Marques Neto', cpf='12345678901',
                    email='luizneto79@gmail.com', phone='51-99999-9999')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expected = 'Confirmação de inscrição'
        self.assertEqual(expected, self.email.subject)

    def test_subscription_email_from(self):
        expected = 'luiz.neto@resale.com.br'
        self.assertEqual(expected, self.email.from_email)

    def test_subscription_email_to(self):
        expected = ['luiz.neto@resale.com.br', 'luizneto79@gmail.com']
        self.assertEqual(expected, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Luiz Marques Neto',
            '12345678901',
            'luizneto79@gmail.com',
            '51-99999-9999',
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
