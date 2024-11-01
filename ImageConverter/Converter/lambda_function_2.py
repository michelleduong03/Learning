import io
import base64
import json
from PIL import Image

def lambda_handler(event, context):
    try:
        # decode the base64 image from JSON body
        body = json.loads(event['body'])
        image_data = base64.b64decode(body['image'])

        # convert the image from WebP to JPEG
        input_image = Image.open(io.BytesIO(image_data))
        output_image_io = io.BytesIO()
        input_image.convert("RGB").save(output_image_io, format="JPEG")
        output_image_io.seek(0)

        # convert output to base64 for response
        output_image_base64 = base64.b64encode(output_image_io.getvalue()).decode('utf-8')

        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
            },
            'body': json.dumps({'image': output_image_base64})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"Error: {str(e)}"
        }
