from django.urls import path
from .views import blog_list

urlpatterns = [
    path('', blog_list),
    path('blog/', blog_list, name='blog_list')
]