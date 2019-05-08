from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.urls import resolve
from ..views import signup
from ..forms import SignUpForm

class SignUpTests(TestCase):
	def setUp(self):
		url= reverse('signup')
		response = self.client.get(url)

	def signup_statuscode:
		self.assertEquals(response.status_code, 200)

	def signupurl_gives_signupview(self):
		view=resolve('/signup/')
		self.assertEquals(view.func, signup)

	def csrf_check(self):
		self.assertContains(self.response, 'csrfmiddlewaretoken')

	def contains_form(self):
		form= self.response.context.get('form')
		self.assertIsInstance(form, SignUpForm)

	def test_form_inputs(self):
		self.assertContains(self.response, '<input', 5)
		self.assertContains(self.response, 'type="text"', 1)
		self.assertContains(self.response, 'type="email"', 1)
		self.assertContains(self.response, 'type="password"', 2)

class successful_signup_tests(TestCase):
	def setUp(self):
		url= reverse('signup')
		data= {'username':'mythili', 'email':'mythilirajendra@rediffmail.com' ,'password1':'mythili1234', 'password2':'mythili1234'}
		self.response= self.client.post(url, data)
		self.home_url= reverse('home')

	def redirection(self):
		self.assertRedirects(self.response, self.home_url)

	def user_creation(self):
		self.assertTrue(User.objects.exists())

	def user_authentication(self):
		response= self.client.get(self.home_url)
		user= response.context.get('user')
		self.assertTrue(user.is_authenticated)

class invalid_signup_tests(TestCase):
	def setUp(self):
		url= reverse('signup')
		self.response= self.client.post(url, {})

	def signup_statuscode(self):
		self.assertEquals(self.response.status_code, 200)

	def form_errors(self):
		form= self.response.context.get('form')
		self.assertTrue(form.errors)

	def dont_create_user(self):
		self.assertFalse(User.objects.exists())

