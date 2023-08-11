from django.urls import path
from . import views

urlpatterns = [
    path("menu/", views.get_menu_items_api, name="menu_list"),
    path("menu/create/", views.create_menu_item_api, name="create_menu_item"),
    path(
        "menu/update/<str:item_id>/",
        views.update_menu_item_api,
        name="update_menu_item",
    ),
    path(
        "menu/delete/<str:item_id>/",
        views.delete_menu_item_api,
        name="delete_menu_item",
    ),
]
