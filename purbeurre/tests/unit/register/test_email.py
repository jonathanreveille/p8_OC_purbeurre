from django.test import TestCase
from django.core import mail as m


class EmailSenderUnitTest(TestCase):

    m.outbox = []

    def test_send_email(self):
        """Send message via ou django application"""
        m.send_mail(
            "Example subject here",
            "Body message is here",
            "purbeurre@purberre.com",
            ["user@mail.com"],
            fail_silently = False,
        )

        self.assertEqual(len(m.outbox), 1)
        self.assertEqual(m.outbox[0].subject,"Example subject here")
        self.assertEqual(m.outbox[0].body,"Body message is here")
        self.assertEqual(m.outbox[0].from_email,"purbeurre@purberre.com")
        self.assertEqual(m.outbox[0].to, ["user@mail.com"])

        #https://timonweb.com/django/testing-emails-in-django/
        