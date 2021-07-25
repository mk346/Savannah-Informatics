from django.urls import path
from .views import home, review,GenericAPIView


urlpatterns = [
    path('',home,name='home'),
    path('review/',review,name='review'),
    path('generic/',GenericAPIView.as_view()),
    path('generic/<int:id>/',GenericAPIView.as_view()),
    

]