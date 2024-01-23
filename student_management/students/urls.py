from django.urls import path
from students import views


urlpatterns = [
    path('all_students/', views.students_all, name = 'all_students'),
    path('add_students/', views.add_students, name = 'add_students'),
    path('update_students/', views.update_students, name = 'update_students'),
    path('remove_students/', views.remove_students, name = 'remove_students'),
    # path('update/', views.update_students, name = 'update'),
    path('update_by_roll_number/<str:roll_number>', views.update_by_roll_number, name = 'update_by_roll_number'),
]
