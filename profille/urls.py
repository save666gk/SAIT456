from django.urls import path, include

from profille import views
app_name = 'profille'

urlpatterns = [
    path('prof/', views.prof, name='prof'),
    path('glav/', views.glav, name='glav'),
    path('drova/', views.drova, name='drova'),
    path('oplata/', views.oplata, name='oplata'),
    path('buy/<int:product_id>/', views.buy_product, name='buy_product'),
    path('success/', views.success_page, name='success_page'),
    path('send-test-email/', views.send_test_email),
]