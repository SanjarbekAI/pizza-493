from django.urls import path
from pages.views import home_page_view, reserve_view

app_name = 'pages'

urlpatterns = [
    path('reserve/', reserve_view, name='reserve'),
    path('', home_page_view, name='home'),
]