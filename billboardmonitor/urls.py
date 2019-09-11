"""billboardmonitor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token
from django.conf import settings
from django.conf.urls.static import static
from bmonitor.views import BillBoardPost, BillBoardBrandPost, CompetitorPost, ImagePost, BillBoardViewAll, BrandAgencyViewAll, BrandViewAll, MediaAgencyViewAll, BoardSupplierViewAll, ImageViewAll, ImageViewOne

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^auth-jwt/', obtain_jwt_token),
    url(r'^auth-jwt-refresh/', refresh_jwt_token),
    url(r'^auth-jwt-verify/', verify_jwt_token),

    path(r'bill/board/create', BillBoardPost.as_view(), name='create_billboard'),
    path(r'bill/board/all', BillBoardViewAll.as_view(), name='retrieve_billboard'),

    path(r'board/brand/create', BillBoardBrandPost.as_view(),
         name='create_board_brand'),
    path(r'board/competition/create',
         CompetitorPost.as_view(), name='create_competition'),
    path(r'board/image/create', ImagePost.as_view(), name='attach_image'),
    path(r'board/image/all', ImageViewAll.as_view(), name='retrieve_image'),
    path(r'agency/brand/all', BrandAgencyViewAll.as_view(),
         name='retrieve_brandagency'),
    path(r'board/brand/all', BrandViewAll.as_view(), name='retrieve_brand'),
    path(r'media/agency/all', MediaAgencyViewAll.as_view(),
         name='retrieve_agencies'),
    path(r'board/suppliers/all', BoardSupplierViewAll.as_view(),
         name='retrieve_suppliers')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
