from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('all/',views.all_emp),
    path('add/',views.add_emp),
    path('remove/',views.remove_emp1,name="remove"),
    path('remove1/<int:pk>',views.remove_emp,name="remove1"),
    path('filter/',views.filter_emp),
    path('api/',include('empapp.api.urls'))
]
