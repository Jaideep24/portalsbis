"""portalsbis URL Configuration

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
from sbis.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home),
    #path("teacher",teacher),
    path("upload_circular",circular_form.as_view()),
    path("upload_worksheet",worksheet_form.as_view()),
    path("upload",submit_form.as_view()),
    path("viewlist",worksheet),
    path("circular",circular)
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
