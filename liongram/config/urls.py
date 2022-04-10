from django.contrib import admin
from django.urls import path, include

from posts.views import index, url_view, url_parameter_view, function_view, ClassView, function_list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('__debug__/', include('debug_toolbar.urls')),
    path('url/', url_view),
    path('url/<str:username>/', url_parameter_view),
    path('fbv/list/', function_list_view),
    path('fbv/', function_view),
    path('cbv/', ClassView.as_view(), name='cbv'),

    path('', index, name='index'),
    path('posts/', include('posts.urls', namespace='posts')),
]



