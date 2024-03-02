#from django.urls import path

#from . import views

#app_name = 'rides'
#urlpatterns = [
 #   path('', views.splash_page, name='index'),  # Splash page
  #  path('/rides', views.index, name='index_view'),  # Rides listing
   # path('/create', views.create, name='create'),  # Create ride
#]

from django.urls import path
from . import views

app_name = 'rides'
urlpatterns = [
    path('', views.splash_page, name='splash_page'),  # Splash page at the root URL
    path('rides/', views.index, name='index'),  # Rides listing page
    path('create/', views.create, name='create'),  # Create ride page

]