from django.urls import path
from courses.views import CourseView, CourseListView, CourseCreateView, CourseUpdateView, CourseDeleteView

app_name = 'courses'
urlpatterns = [
    path('', CourseListView.as_view(), name='course_list'),
    path('create/', CourseCreateView.as_view(), name='course_create'),
    path('<int:id>/', CourseView.as_view(), name='course_detail'),
    path('<int:id>/update/', CourseUpdateView.as_view(), name='course_update'),
    path('<int:id>/delete/', CourseDeleteView.as_view(), name='course_delete'),
    # goes over url routing based on the path <int:id> will configure different ids
]