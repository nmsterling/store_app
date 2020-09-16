from django.test import Client, TestCase
from api.models import Profile, Products, Reviews, TransactionsHistory, Cart

# Create your tests here.

class LogoutTestCase(TestCase):
    
    def test_logout_redirects_correct_status_code(self):
        c = Client()
        response = c.get('/logout/')
        self.assertEqual(response.status_code, 302)

class UserProfileTestCase(TestCase):
   
    def test_account_renders_correct_status_code(self):
        c = Client()
        response = c.get('/account/')
        self.assertEqual(response.status_code, 200)

    def test_account_renders_correct_template(self):
        c = Client()
        response = c.get('/account/')
        self.assertTemplateUsed(response, 'app/account.html')

    # def test_account_returns_correct_content(self):
    #     data = {'id': 'user id', 'user': 'user name', 
    #             'address': 'user address', 'preferred': 
    #             'user status'}
    #     user = Profile.objects.get()
    #     self.assertDictEqual(data, {'id': user.id,
    #                                 'user': user.user,
    #                                 'address': user.adress,
    #                                 'preferred': user.preferred})

