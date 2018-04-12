#ADRIAN
import datetime
from django.utils import timezone
from django.test import TestCase
from .models import Question, Choice


class QuestionModelTests(TestCase):

	fixtures = ['polls_testdata.json']

	def test_fixture(self):
		self.assertEqual(Question.objects.all().count(), 1)
		self.assertEqual(Choice.objects.all().count(), 6)

	def test_was_published_recently_with_future_question(self):
		time = timezone.now() + datetime.timedelta(days=60)
		future_question = Question(pub_date=time)
		self.assertIs(future_question.was_published_recently(),False)

	def test_was_published_recently_with_old_question(self):
		time = timezone.now() - datetime.timedelta(days=1,seconds=1)
		old_question = Question(pub_date=time)
		self.assertIs(old_question.was_published_recently(),False)

	def test_was_published_recently_with_recent_question(self):
		time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
		recent_question = Question(pub_date=time)
		self.assertIs(recent_question.was_published_recently(),True)

	def test_get_choices(self):
		question = Question.objects.get(pk=2)
		self.assertEqual(question.get_choices(),list(Choice.objects.all()))

	def test_get_leading_choice(self):
		question = Question.objects.get(pk=2)
		self.assertEqual(question.get_leading_choice(),max(question.get_choices()))

	def test_get_leading_choice(self):
		question = Question.objects.get(pk=2)
		pct = question.get_leading_choice_pct()
		self.assertEqual(question.get_leading_choice_pct(), pct)
