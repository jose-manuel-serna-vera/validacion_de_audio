import json
import pytesseract
from PIL import Image


def hello(event, context):

    body = {
        "text": pytesseract.image_to_string(Image.open('image.jpg'),config='--psm 11'
        ),
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    
    return response

#resp=hello("","")
#print(resp)