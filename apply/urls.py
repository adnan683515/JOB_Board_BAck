from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter() # amader router

router.register('applylist', views.ApplyViewSet) # router er antena
router.register('newapply',views.apply_success_hote_hobe,basename='asdfasdfsadf')
urlpatterns = [
    path('', include(router.urls)),

    
    path("applylistedit/<int:pk>/",views.Edit_for_status_view.as_view(),name="edit"),
    path("deleteapply/<int:pk>/",views.delete_view_apply.as_view(),name="delete"),
    path('applistapiview/',views.applyListApiview.as_view()),
    path("apply_deatils/<int:id>/",views.apply_details_retreive.as_view())
    
    
    
]