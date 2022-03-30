"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('hello', views.hello),
    re_path(r'^upload/(?P<did>[a-zA-Z0-9]{32})$', views.upload),
    path('request', views.request),
    path('get_documents', views.get_documents),
    path('get_document', views.get_document),
    path('get_document_requests', views.get_document_requests),
    path('download', views.download),
    path('upload_html', views.render_upload_html),
    path('download_html', views.render_download_html),
]
