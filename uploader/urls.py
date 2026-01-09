from django.urls import path
from .views import upload_file, file_list

urlpatterns = [
    path('/upload/', upload_file, name='upload_file'),   # y naam uplad_file imp hota hai redirect karne m kaam ata hai 
    path('/files/', file_list, name='file-list'),
]
