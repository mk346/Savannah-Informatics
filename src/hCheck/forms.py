from django import forms
from django.forms import ModelForm
from .models import healthSys

# create form
class myForm(ModelForm):
	class Meta:
		model = healthSys
		fields = ('hName', 'county', 'system', 'sVersion')
		labels = {
		    'hName': '',
		    'county': '',
		    'system': '',
		    'sVersion': '',

		}
		widgets = {
		    'hName':forms.TextInput(attrs={'class':'form-control', 'Placeholder':'Hospital Name' }),
		    'county':forms.TextInput(attrs={'class':'form-control', 'Placeholder':'County' }),
		    'system':forms.TextInput(attrs={'class':'form-control','Placeholder':'System Installed' }),
		    'sVersion': forms.TextInput(attrs={'class':'form-control','Placeholder':'System Version' }),

		}

