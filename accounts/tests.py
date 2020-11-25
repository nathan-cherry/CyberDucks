from django.test import TestCase
from .models import Task, User, Project

'''
Template for test:

from .models import X
class XTestCase(TestCase):
    def test_X_Something(self):
        test_X = X(*Insert needed fields for instatiation*)
        self.assertEqual(test_X.*Insert some method or attribute*, WhateverBeingTestedShouldEqual)

run all tests by running:
python manage.py test
'''

# Create your tests here.
class TaskTestCase(TestCase):
    def test_create_task(self):
        test_user = User()
        test_project = Project()
        test_task = Task(id=None, title='tester', description='test', status='OPN', start_date='', end_date='',
                        assigned_to=test_user, date_created='', priority='LW', project=test_project)
        self.assertEqual(test_task.title, 'tester')