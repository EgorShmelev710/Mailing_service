from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import MailingListView, ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, \
    ClientDeleteView

app_name = MailingConfig.name

urlpatterns = [
    path('', MailingListView.as_view(), name='home'),
    path('client_list/', ClientListView.as_view(), name='clients'),
    path('client_detail/<int:pk>/', ClientDetailView.as_view(), name='view_client'),
    path('client_create/', ClientCreateView.as_view(), name='create_client'),
    path('client_update/<int:pk>/', ClientUpdateView.as_view(), name='update_client'),
    path('client_delete/<int:pk>/', ClientDeleteView.as_view(), name='delete_client'),
]
