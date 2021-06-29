from django.urls import path
from .views import (
     LeadListView,
     LeadCreateView,
     LeadDeleteView,
     LeadUpdateView,
     LeadDetailView)


app_name = 'leads'

urlpatterns = [
    path('' , LeadListView.as_view() , name='lead-list'),
    path('update/<int:pk>/' , LeadUpdateView.as_view() , name='lead-update'),
    path('delete/<int:pk>/' , LeadDeleteView.as_view() , name='lead-delete'),
    path('<int:pk>/' , LeadDetailView.as_view() , name='lead-detail'),
    path('create/' , LeadCreateView.as_view() , name='lead-create')
]
