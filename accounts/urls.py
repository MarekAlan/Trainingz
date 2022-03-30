from django.urls import path
from accounts import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('users_list/', views.UserListView.as_view(), name='users_list'),
    path('user_perm/<int:id>/', views.UserPermSettingView.as_view, name='user_perm'),
]
