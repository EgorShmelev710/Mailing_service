from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import MailingListView, ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, \
    ClientDeleteView, MailingDetailView, MailingCreateView, MailingUpdateView, MailingDeleteView

app_name = MailingConfig.name

urlpatterns = [
    path('', MailingListView.as_view(), name='home'),
    path('mailing_detail/<int:pk>/', MailingDetailView.as_view(), name='view_mailing'),
    path('mailing_create/', MailingCreateView.as_view(), name='create_mailing'),
    path('mailing_update/<int:pk>/', MailingUpdateView.as_view(), name='update_mailing'),
    path('mailing_delete/<int:pk>/', MailingDeleteView.as_view(), name='delete_mailing'),

    path('client_list/', ClientListView.as_view(), name='clients'),
    path('client_detail/<int:pk>/', ClientDetailView.as_view(), name='view_client'),
    path('client_create/', ClientCreateView.as_view(), name='create_client'),
    path('client_update/<int:pk>/', ClientUpdateView.as_view(), name='update_client'),
    path('client_delete/<int:pk>/', ClientDeleteView.as_view(), name='delete_client'),
]
