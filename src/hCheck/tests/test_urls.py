from django.test import SimpleTestCase
from django.urls import reverse, resolve
from hCheck.views import home, review

class TestUrls(SimpleTestCase):
	# function to test the home url
	def test_home_url_is_resolved(self):
		url = reverse('home')
		print(resolve(url))
		self.assertEquals(resolve(url).func, home)
    
    # function to test the review url
	def test_review_url_is_resolved(self):
		url = reverse('review')
		print(resolve(url))
		self.assertEquals(resolve(url).func, review)
		
		
