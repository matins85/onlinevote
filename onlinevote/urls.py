"""Furnisheet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from allauth.account import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from accounts import views

schema_view = get_schema_view(
    openapi.Info(
        title="ONLINEVOTE Services API",
        default_version='v1',
        description="ONLINEVOTE Services",
    ),
)

urlpatterns = [
    path('', views.index, name="index"),
    # Swagger Docs
    path('swagger-docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # Admin
    path('admin/', admin.site.urls),
    # Accounts
    path('accounts/', include('accounts.urls')),
    # Rest Auth
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/accounts/login/', views.UserLoginView.as_view(), name='custom-login'),
    path('rest-auth/facebook/', views.FacebookLogin.as_view(), name='fb_login'),
    path('rest-auth/google/', views.GoogleLogin.as_view(), name='google_login'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
