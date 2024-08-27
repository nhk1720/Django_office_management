from django.urls import path,include
from empapp.api import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('dept',views.Emp_Dept, basename='dept')
router.register('role',views.Role_Dept, basename='role')
router.register('employe',views.Emp_Details, basename='Emp_Details')
urlpatterns = [
    path('',include(router.urls))
]
