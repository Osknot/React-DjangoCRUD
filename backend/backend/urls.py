from django.contrib import admin
from django.urls import path, include
from api.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),  # This is the noraml admin panel
    # this is for the create user view, it will be used to register a new user, it will be accessed by the frontend when the user submits the registration form, it will return the user object in response if the registration is successful, otherwise it will return the error message in response
    path("api/user/register/", CreateUserView.as_view(), name="register"),
    # this is for the token obtain pair view, it will be used to get the access and refresh token, it will be accessed by the frontend when the user submits the login form, it will return the access and refresh token in response if the login is successful, otherwise it will return the error message in response
    path("api/token/", TokenObtainPairView.as_view(), name="get_token"),

    # this is for the token refresh view, it will be used to refresh the access token, it will be accessed by the frontend when the access token is expired, it will return the new access token in response if the refresh token is valid, otherwise it will return the error message in response
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    # this is for the browsable api, it will be used to access the browsable api, it will be accessed by the frontend when the user wants to access the browsable api, it will return the browsable api in response if the user is authenticated, otherwise it will return the login page in response
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include("api.urls")),

]
# For each of the routes, it should be that you will check for all the pages if you requrire login or not and that is how you should build from there, for example the registration and login page should not require login but the dashboard page should require login, so you will build the frontend accordingly and then you will build the backend accordingly, for example for the dashboard page you will create a view that will return the data for the dashboard page and you will set the permission class to IsAuthenticated so that only authenticated users can access that view, and then you will create a route for that view in the urls.py file and then you will access that route from the frontend when the user wants to access the dashboard page.
