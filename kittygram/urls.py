from django.urls import path

from cats.views import cat_list, api_cat_detail

urlpatterns = [
   path('cats/', cat_list),
   path('cats/<int:pk>/', api_cat_detail),
]
