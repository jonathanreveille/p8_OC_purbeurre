from django.test import TestCase, Client
from django.core import mail as m
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.forms import PasswordResetForm


class EmailSenderUnitTest(TestCase):

    def setUp(self):

        m.outbox = []

        self.user = User.objects.create_user(
                                    username="Foodlover12",
                                    password="testing123321",
                                    email="foodmaniatest@gmail.com"
                                    )

    def test_if_reset_password_works(self):
        """test if user can receive email to reset
        password"""

        # response = self.client.get(reverse('password_reset'))
        response = self.client.get(reverse('password_reset'))

        with open("templates/registration/password_reset_subject.txt","r") as subject:
            email_subject = str(subject.read())
        
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
        self.assertEqual(m.outbox[0].subject,"PurBeurre - Réinitialisation de votre mot de passe")


    # def setUp(self):
    #     """creating a fictive user, and we will use
    #     him to send a reset email"""
        
    #     m.outbox = []

    #     self.email_user = PasswordResetForm( 
    #         "foodlovemaniac@gmail.com"
    #         )
    #     # self.user = User.objects.create_user(
    #     #     username = "Testing_user_for_email",
    #     #     email = self.email_user,
    #     #     password = "1212testing2323",
    #     # )

    # def test_to_check_email_field(self):
    #     """test to check if the email is the same
    #     as the users"""
    #     self.assertEquals(self.email_user, "foodlovemaniac@gmail.com")

    # def test_send_email_to_user_v1(self):
    #     """test to see if the message sent will
    #     call the template created to reset 
    #     password of the user"""

    #     # une histoire avec POST (pour envoyer que GET >> pour recevoir une info)
    #     m.send_mail("Example of subject here",
    #                 "changement de votre mot de passe",
    #                 "purbeurre@purbeurre.com",
    #                 [self.email_user]
    #                 )

    #     self.assertIn(m.outbox[0].body,"changement de votre mot de passe")
    #     self.assertEqual(m.outbox[0].to, [self.user.email])


    # def test_send_email_to_user_v2(self):
    #     """test to see if the message sent will
    #     call the template created to reset 
    #     password of the user"""

    #     if request.method.post(reverse("password_reset")):

    #     m.send_mail("Réinitialisation",
    #                 "changement de votre mot de passe",
    #                 "purbeurre@purbeurre.com",
    #                 [self.user.email]
    #                 )

    #     self.assertEqual(m.oubox[0].template, "password_reset_email.html")
    #     self.assertIn(m.outbox[0].body,"changement de votre mot de passe")
    #     self.assertEqual(m.outbox[0].to, [self.user.email])

# une histoire avec POST (pour envoyer que GET >> pour recevoir une info)

# REDO THIS TESTING UDER. DO IT ABOVE FROM THIS LINE
    # def test_send_email(self):
    #     """Send message via ou django application"""
    #     m.send_mail(
    #         "Example subject here",
    #         "Body message is here",
    #         "purbeurre@purberre.com",
    #         ["user@mail.com"],
    #         fail_silently = False,
    #     )

    #     self.assertEqual(len(m.outbox), 1)
    #     self.assertEqual(m.outbox[0].subject,"Example subject here")
    #     self.assertEqual(m.outbox[0].body,"Body message is here")
    #     self.assertEqual(m.outbox[0].from_email,"purbeurre@purberre.com")
    #     self.assertEqual(m.outbox[0].to, ["user@mail.com"])

        #https://timonweb.com/django/testing-emails-in-django/
        