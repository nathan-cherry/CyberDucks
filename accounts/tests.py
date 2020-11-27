from urllib.parse import urlencode

from django.test import TestCase
from .models import *

'''
Template for test:

from .models import X
class XTestCase(TestCase):
    def test_X_Something(self):
        test_X = X(*Insert needed fields for instantiation*)
        self.assertEqual(test_X.*Insert some method or attribute*, WhateverBeingTestedShouldEqual)

run all tests by running:
python manage.py test
'''


# Blair
class TaskTestCase(TestCase):
    def test_create_task(self):
        test_user = User()
        test_project = Project()
        test_task = Task(id=None, title='tester', description='test', status='OPN', start_date='', end_date='',
                         assigned_to=test_user, date_created='', priority='LW', project=test_project)
        self.assertEqual(test_task.title, 'tester')


# Nathan
class AccountCreationTestCase(TestCase):
    def setUp(self):
        # credentials
        self.credentials = {
            'username': 'test_user',
            'password': 'secret'
        }
        # Create user
        user = User.objects.create_user(**self.credentials)
        # Log user in
        login = self.client.login(username='test_user', password='secret')
        # Checks if login successful
        self.assertEqual(login, True)
        # Check if logged in user is the newly created user
        self.assertEqual(int(self.client.session['_auth_user_id']), user.pk)

    def test_login(self):
        # This will send the credentials to the '/login/' path (urls.py) which calls the loginPage function in views.py
        # since the request method is post, the function will attempt to login the user
        data = urlencode({'username': 'test_user', 'password': 'secret'})
        response = self.client.post('/login/', data, content_type="application/x-www-form-urlencoded", follow=True)
        # Test that the authentication worked and the user was created and signed in
        self.assertEqual(response.context['user'].is_authenticated, True)

    def test_logout(self):
        # Log in to user
        login = self.client.login(username='test_user', password='secret')
        # Check that login successful
        self.assertEqual(login, True)
        # Send request to the logout method
        response = self.client.get('/logout/', follow=True)
        # Check that the user is not authenticated
        self.assertEqual(response.context['user'].is_authenticated, False)
