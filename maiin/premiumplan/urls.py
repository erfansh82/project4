from django.urls import path
from premiumplan import views

app_name='plan'
urlpatterns = [
    path('plan-list/',views.PlanList.as_view()),
    path('create-plan/',views.CreatePlanView.as_view()),
    path('update-plan/<int:pk>/',views.EditPlanView.as_view()),
    path('delete-plan/<int:pk>/',views.DeletePlanView.as_view()),
    path('hide-plan/',views.HidePlanView.as_view()),
    path('show-plan/',views.ShowPlanView.as_view()),
]
