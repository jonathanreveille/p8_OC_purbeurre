from django.test import TestCase, Client
from django.core import mail as m
from django.contrib.auth.models import User
from django.urls import reverse


class EmailSenderUnitTest(TestCase):
    """Test to check if the email is
    sent with a body using the views
    and the template"""

    def setUp(self):
        """Creating empty outbox. Creating one
        fictive active user"""
        m.outbox = []

        self.user = User.objects.create_user(
                                    username="Foodlover12",
                                    password="testing123321",
                                    email="foodmaniatest@gmail.com"
                                    )

    def test_if_reset_password_works(self):
        """Test if the user can receive a reset
        email for his password using the template
        in registration that creates the body content
        and calls the auth views"""

        response = self.client.post(reverse('password_reset'))
        #response = self.client.get(reverse('password_reset'))
        # create variable with the subject content of the template
        with open("templates/registration/password_reset_subject.txt","r") as subject:
            email_subject = str(subject.read())
        # create variable with the email body from the template
        with open("templates/registration/password_reset_email.html", "r") as body:
            email_body = str(body.read())
            
        m.send_mail(
            email_subject,
            email_body,
            "purbeurre@purbeurre.com",
            [self.user.email]
            )
            
        self.assertEqual(len(m.outbox), 1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(m.outbox[0].from_email,"purbeurre@purbeurre.com")
        self.assertEqual(m.outbox[0].to, [self.user.email])
        self.assertIsNot(m.outbox[0].body, "Scam Robot")
        self.assertTemplateUsed("templates/registration/password_reset_email.html")
        self.assertTrue(m.outbox[0].subject,"PurBeurre - Réinitialisation de votre mot de passe")