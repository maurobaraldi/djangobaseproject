from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from vendors import views

urlpatterns = [
    path("", views.VendorsList.as_view(), name="vendor"),
    path("<int:pk>/", views.VendorsDetail.as_view(), name="vendor-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
