from django.urls import path, include
from . import views

urlpatterns = [
    # path('api/crawl/<str:hashtag_value>/', views.crawl, name='crawl'),
    # path('api/show/<str:hashtag_value>/', views.show_data, name='show')
    path('api/crawl/<str:hashtag_value>/', views.crawl, name='crawl'),
    path('api/show/<str:hashtag_value>/', views.show_data, name='show')
]
