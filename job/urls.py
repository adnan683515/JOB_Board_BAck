from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter() # amader router

router.register('joblist', views.job_Viewset) # router er antena
router.register('companys',views.companyViewSet)
urlpatterns = [
    path('', include(router.urls)),
    # path('joblist/',views.JOBtList.as_view())
    path('alll_Job_get/',views.JOb_view_set_get.as_view()),
    path('job_detail/<int:id>/',views.single_job_retrive.as_view())
    
    
]