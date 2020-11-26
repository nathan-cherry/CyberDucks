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
    def test_create_user(self):
        # Create user
        self.user = User.objects.create_user(username='test_user', password='12345')
        # Log user in
        login = self.client.login(username='test_user', password='12345')
        # Checks if login successful
        self.assertEqual(login, True)
        # Check if logged in user is the newly created user
        self.assertEqual(int(self.client.session['_auth_user_id']), self.user.pk)
