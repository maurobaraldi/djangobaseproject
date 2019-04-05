from django.urls import include, path

urlpatterns = [
    path('vendors/', include('vendors.urls')),
    path('users/', include('users.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
