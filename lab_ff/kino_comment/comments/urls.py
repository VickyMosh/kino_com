from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),   #при переходе на гл стр обращаемся к методу индекс в вью
    path('movies', views.movie, name='movie'),
    path('cartoons', views.cartoon, name='cartoon'),
    path('outlog', views.outlog, name='outlog')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
