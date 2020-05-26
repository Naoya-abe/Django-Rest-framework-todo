from django.urls import path, include

from rest_framework.routers import DefaultRouter

from todo_api import views


router = DefaultRouter()
router.register('users', views.UserViewSet)
router.register('todos', views.TodoItemViewSet)

urlpatterns = [
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]
