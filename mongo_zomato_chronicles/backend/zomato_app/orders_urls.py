from django.urls import path
from . import views

urlpatterns = [
    path("orders/", views.get_orders_items_api, name="orders_list"),
    path(
        "orders/create/", views.create_orders_item_api, name="create_orders_item"
    ),
    path(
        "orders/update/<str:item_id>/",
        views.update_orders_status_item_api,
        name="update_orders_item",
    ),
    path(
        "orders/delete/<str:item_id>/",
        views.delete_orders_item_api,
        name="delete_orders_item",
    ),
]
