from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('check-result/', views.CheckResultView.as_view(), name='check_result'),
    path('profile/', views.ProfileDetailsView.as_view(), name='profile_details'),
    path('average-chart/', views.AverageChartView.as_view(), name='average_chart'),
    path('info/', views.InfoPageView.as_view(), name='info_page_view')
]