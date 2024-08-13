
from django.urls import path
from . import views
from .views import case_detail, news_detail

urlpatterns = [
    path('', views.index, name='home'),
    path('page2/', views.page2, name='page2'),
    path('page3/', views.page3, name='page3'),
    path('page4/', views.page4, name='page4'),
    path('case/<int:case_id>/', case_detail, name='case_detail'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),
    path('page5/', views.page5, name='page5'),
    path('send_email/', views.send_email, name='send_email'),
]
