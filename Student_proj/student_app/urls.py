from django.urls import path
from . import views

app_name = 'student_app'

urlpatterns = [
    path('list/',views.StudentListView.as_view(),name='student_list'),
    path('edit/<int:pk>/',views.StudentUpdateView.as_view(),name='student_edit'),
    path('delete/<int:pk>/',views.StudentDeleteView.as_view(),name='student_delete'),
    path('add/',views.StudentCreateView.as_view(),name='student_add'),
        
]