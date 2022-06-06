from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import SearchResultsView

urlpatterns = [
    path('', views.index, name='home'),  # при переходе на гл стр обращаемся к методу индекс в вью
    path('movies', views.movie, name='movie'),
    path('cartoons', views.cartoon, name='cartoon'),
    path('outlog', views.outlog, name='outlog'),
    path('leon_full', views.leon_full, name='leon_full'),
    path('koko_full', views.koko_full, name='koko_full'),
    path('soul_full', views.soul_full, name='soul_full'),
    path('pirates_full', views.pirates_full, name='pirates_full'),
    path('dolmatines_full', views.dolmatines_full, name='dolmatines_full'),
    path('wishes_full', views.wishes_full, name='wishes_full'),
    path('search/', SearchResultsView.as_view(), name='search_results'),

    path('film/<int:pk>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('list/', views.MovieListView.as_view(), name='movie_list'),
    path('<int:film_id>/add_comment/', views.add_comment, name='add_comment'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
