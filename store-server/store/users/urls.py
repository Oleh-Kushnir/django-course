from django.urls import path
from django.contrib.auth.decorators import login_required


from users.views import UserLoginView, UserProfileView, UserRegistrationView, EmailVerificationView, UserLogoutView

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('profile/<int:pk>', login_required(UserProfileView.as_view()), name='profile'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('verify/<str:email>/<uuid:code>/', EmailVerificationView.as_view(), name='email-verification'),
]
