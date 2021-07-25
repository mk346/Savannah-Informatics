from django.test import TestCase, Client
from django.urls import reverse
from hCheck.models import healthSys




class TestViews(TestCase):
	def setUp(self):
		self.client = Client()
		self.home_url = reverse('home')
		self.review_url = reverse('review')


    # function to test the home view
	def test_home_GET(self):
		response = self.client.get(self.home_url)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response,'hCheck/index.html')

    # function to test the review view 
	def	test_review_GET(self):
		response = self.client.get(self.review_url )

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'hCheck/review.html')
