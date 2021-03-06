from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.index, name='home'),  # при переходе на гл стр обращаемся к методу индекс в вью
                  path('movies', views.movie, name='movie'),
                  path('outlog', views.outlog, name='outlog'),
                  path('search/', views.SearchResultsView.as_view(), name='search_results'),

                  path('add', views.add, name='add'),
                  path('delete', views.delete, name='delete'),
                  path('edit', views.edit, name='edit'),

                  path('film/<int:pk>/', views.MovieDetailView.as_view(), name='movie_detail'),
                  path('list/', views.MovieListView.as_view(), name='movie_list'),
                  path('<int:film_id>/add_comment/', views.add_comment, name='add_comment'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
