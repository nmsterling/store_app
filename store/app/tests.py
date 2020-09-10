from django.test import Client, TestCase
from api.models import Profile, Products, Reviews, TransactionsHistory, Cart

# Create your tests here.

class UserProfileTestCase(TestCase):
   
    def test_account_renders_correct_status_code(self):
        c = Client()
        response = c.get('/account/')
        self.assertEqual(response.status_code, 200)

    def test_account_renders_correct_template(self):
        c = Client()
        response = c.get('/account/')
        self.assertTemplateUsed(response, 'app/account.html')