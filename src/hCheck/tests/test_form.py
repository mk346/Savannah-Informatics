from django.test import SimpleTestCase
from hCheck.forms import myForm


class TestForms(SimpleTestCase):

    # function to test whether the form is valid
	def test_myForm_valid_data(self):
		# intializing test data for the form fields
		form = myForm(data={
			'hName': 'Nairobi Hospital',
			'county': 'Nairobi',
			'system': 'Ushauri',
			'sVersion': '10.1.3.4',
			})

		self.assertTrue(form.is_valid())
		
    # function to test whether the form is invalid
	def test_myForm_no_data(self):
		form = myForm(data={})

		self.assertFalse(form.is_valid())
		self.assertEquals(len(form.errors), 2) # to check whether the 2 required fields have been filled first

