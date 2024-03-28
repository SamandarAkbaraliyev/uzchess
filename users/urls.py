from django.urls import path

from users.views import user_detail_view, user_redirect_view, user_update_view, GoogleLogin
from users.api.views import RegisterAPI
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = "users"

urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path('register/', RegisterAPI.as_view()),
    # path('google/', GoogleLogin.as_view(), name='go_login'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path("<str:username>/", view=user_detail_view, name="detail"),


]
