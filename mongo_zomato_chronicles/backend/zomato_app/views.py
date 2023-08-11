from bson import ObjectId
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .mongo_connection import db
from rest_framework import status
from django.utils import timezone


@api_view(["GET"])
def get_menu_items_api(request):
    try:
        menu_collection = db["menu"]
        menu_items = menu_collection.find()
        serialized_menu_items = [
            {
                "id": str(item["_id"]),  # Convert ObjectId to string
                "name": item["name"],
                "price": item["price"],
                "availability": item["availability"],
            }
            for item in menu_items
        ]
        return Response({"menu_items": serialized_menu_items, "success": True})
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
def create_menu_item_api(request):
    try:
        data = request.data
        menu_collection = db["menu"]
        new_item = {
            "name": data["name"],
            "price": data["price"],
            "availability": data["availability"],
        }
        menu_collection.insert_one(new_item)
        return Response(
            {"message": "Menu item created successfully", "success": True},
            status=status.HTTP_201_CREATED,
        )
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["PUT"])
def update_menu_item_api(request, item_id):
    print(item_id)
    try:
        data = request.data
        menu_collection = db["menu"]
        updated_item = {
            "name": data["name"],
            "price": data["price"],
            "availability": data["availability"],
        }
        menu_collection.update_one({"_id": ObjectId(item_id)}, {"$set": updated_item})
        return Response({"message": "Menu item updated successfully", "success": True})
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["DELETE"])
def delete_menu_item_api(request, item_id):
    try:
        menu_collection = db["menu"]
        menu_collection.delete_one({"_id": ObjectId(item_id)})
        return Response({"message": "Menu item deleted successfully", "success": True})
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# order api


@api_view(["POST"])
def create_orders_item_api(request):
    try:
        data = request.data
        orders_collection = db["orders"]
        new_item = {
            "customer_name": data["customer_name"],
            "dishes_ids": data["dishes_ids"],
            "total_price": data["total_price"],
            "status": "recieved",
            "order_date": timezone.now(),
        }
        orders_collection.insert_one(new_item)
        return Response(
            {"message": "orders item created successfully", "success": True},
            status=status.HTTP_201_CREATED,
        )
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
def get_orders_items_api(request):
    try:
        orders_collection = db["orders"]
        orders_items = orders_collection.find()
        serialized_orders_items = [
            {
                "id": str(item["_id"]),
                "customer_name": item["customer_name"],
                "dishes_ids": item["dishes_ids"],
                "total_price": item["total_price"],
                "status": item["status"],
                "order_date": item["order_date"],
            }
            for item in orders_items
        ]
        return Response({"orders_items": serialized_orders_items, "success": True})
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["PUT"])
def update_orders_status_item_api(request, item_id):
    try:
        data = request.data
        orders_collection = db["orders"]
        updated_item = {
            "status": data["status"],
        }
        orders_collection.update_one({"_id": ObjectId(item_id)}, {"$set": updated_item})
        return Response(
            {"message": "orders item updated successfully", "success": True}
        )
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["DELETE"])
def delete_orders_item_api(request, item_id):
    try:
        orders_collection = db["orders"]
        orders_collection.delete_one({"_id": ObjectId(item_id)})
        return Response(
            {"message": "orders item deleted successfully", "success": True}
        )
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)