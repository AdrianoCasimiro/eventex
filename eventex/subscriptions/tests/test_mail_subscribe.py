from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Adriano Casimiro', cpf='33508295893',
                    email='adrianocasi@gmail.com', phone='19 997795446')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'adrianocasi@gmail.com'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['adrianocasi@gmail.com', 'adrianocasi@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Adriano Casimiro',
            '33508295893',
            'adrianocasi@gmail.com',
            '19 997795446'
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)