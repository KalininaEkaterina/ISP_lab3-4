from django.contrib import admin
from django.templatetags.static import static
from django.urls import path, include

from Сайт import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('post.urls'))
]
