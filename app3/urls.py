from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.todofn,name='task'),
    path('delete/<int:id>',views.dlt_task,name='delete'),
    path('update/<int:id>',views.update_task,name='update')
]