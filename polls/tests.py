# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Question, Choice


class QuestionModelTests(TestCase):

    fixtures = ['polls_testdata.json']

    def test_fixture(self):
        self.assertEqual(Question.objects.all().count(), 1)
        self.assertEqual(Choice.objects.all().count(), 6)

