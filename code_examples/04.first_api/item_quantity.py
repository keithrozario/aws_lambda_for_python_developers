import json

# define the item quantities
item_quantity = {
    "Apple": 3,
    "Orange": 5,
    "Lemon": 7
}


def get_item(event, context):

    item = event['queryStringParameters']['item']
    quantity = item_quantity[item]

    api_response = {
        "statusCode": 200,
        "body": {
            "item": item,
            "quantity": quantity
        }
    }

    return api_response