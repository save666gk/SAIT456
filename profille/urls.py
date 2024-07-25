from django.urls import path, include

from profille import views
app_name = 'profille'

urlpatterns = [
    path('prof/', views.prof, name='prof'),
    path('glav/', views.glav, name='glav'),
    path('mybay/', views.mybay, name='mybay'),
    path('bay/', views.bay, name='bay'),
    path('drova/', views.drova, name='drova'),
    path('oplata/', views.oplata, name='oplata'),

]