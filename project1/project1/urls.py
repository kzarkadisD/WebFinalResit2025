# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("", include("app1.urls")),
# 	path("", include("users.urls")),

# ]

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app1.urls')),
    path('', include('users.urls')),
    path('checkout/', views.checkout, name="checkout"),
]