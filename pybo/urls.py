from django.urls import path
from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='index'), # url 별칭부여
    path('<int:question_id>/', views.detail, name='detail'),
]