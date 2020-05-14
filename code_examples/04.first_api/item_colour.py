import json

# define item colors
item_colour = {
    "Apple": "Red",
    "Orange": "Orange",
    "Lemon": "Yellow",
}

def handler(event, context):
    """
    Args:
      event['queryStringParameters']['item']: Item to check colour on
    return:
      colour: Colour of item
      item: Item requested
    """

    item = event['queryStringParameters']['item']
    colour = item_colour[item]

    api_response = {
        "statusCode": 200,
        "body": json.dumps({
            "item": item,
            "colour": colour,
        })
    }

    return api_response