from django.urls import path
from Blog.views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

app_name = 'Blog'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('create/', ArticleCreateView.as_view(), name='article_create'),
    path('<int:id>/', ArticleDetailView.as_view(), name='article_detail'),
    path('<int:id>/update/', ArticleUpdateView.as_view(), name='article_update'),
    path('<int:id>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    # goes over url routing based on the path <int:id> will configure different ids
]