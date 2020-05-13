import json

def get_item(event, context):
    items = ['Apple', 'Oranges' , 'Lemons']
    api_response = {
        "statusCode": 200,
        "body": json.dumps(items)
    }
    return api_response