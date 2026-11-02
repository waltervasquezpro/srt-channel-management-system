from django.urls import path
from .views import home, service_list, service_create,service_edit,service_delete,customer_create_popup,channel_create_popup,UserLoginView,UserLogoutView

urlpatterns = [
    path("", home, name="home"),
    path("services/", service_list, name="service_list"),
    path("services/create/", service_create, name="service_create"),
]
from .views import home, service_list, service_create, service_edit, service_delete

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("", home, name="home"),
    path("services/", service_list, name="service_list"),
    path("services/create/", service_create, name="service_create"),
    path("services/<int:pk>/edit/", service_edit, name="service_edit"),
    path("services/<int:pk>/delete/", service_delete, name="service_delete"),
    path("customers/popup/create/", customer_create_popup, name="customer_create_popup"),
    path("channels/popup/create/", channel_create_popup, name="channel_create_popup"),
]