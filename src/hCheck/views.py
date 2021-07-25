from django.shortcuts import render
from .models import healthSys
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import mySerializer
from rest_framework.decorators import api_view
from .forms import myForm
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# API endpoint that allows updating, modifying ,deleting and adding data into the database
class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
	serializer_class = mySerializer
	queryset = healthSys.objects.all()
	lookup_field = 'id'
	authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [IsAuthenticated]

	def get(self, request, id=None):
		if id:
			return self.retrieve(request)

		else:
			return self.list(request)
            

	def post(self, request):
		return self.create(request)

	def put(self, request, id=None):
		return self.update(request,id)

	def delete(self, request, id):
		return self.destroy(request,id)
		

		





def home(request):
	submitted = False
	if request.method == "POST":
		form = myForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/?submitted=True')
	else:
		form = myForm
		if 'submitted' in request.GET:
			submitted = True
	return render(request, 'hCheck/index.html',{'form':form,'submitted':submitted})		
			
    
# view for the search functionality
def review(request):
	if request.method == "POST":
		search = request.POST['search'].capitalize()
		results = healthSys.objects.filter(hName__contains=search)
		return render(request, 'hCheck/review.html',{'search':search,'results':results})

	else:
		results = ("Not Found")
		return render(request, 'hCheck/review.html',{'results':results})

