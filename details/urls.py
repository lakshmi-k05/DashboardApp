from . import views
from django.urls import path, include

urlpatterns = [
    path('viewdocs/<int:bid>', views.display_doc_view, name='doc_details'),
    #Batch_details page to view batch-wise data
    path('viewdata/', views.display_batch_view, name='batch_details'),
    #Default details page to load data
    path('', views.fill_data_view, name='details'),

]
