import io
from PIL import Image
import base64

def lambda_handler(event, context):
    try:
        # Decode the image from base64
        image_data = base64.b64decode(event['body'])

        # Open the image using PIL
        input_image = Image.open(io.BytesIO(image_data))

        # Convert WebP to JPEG
        output_image_io = io.BytesIO()
        input_image.convert("RGB").save(output_image_io, format="JPEG")
        output_image_io.seek(0)

        # Convert the output image back to base64 to return it
        output_image_base64 = base64.b64encode(output_image_io.getvalue()).decode('utf-8')

        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'image/jpeg',
                'Content-Disposition': 'inline; filename="converted_image.jpg"',
            },
            'body': output_image_base64,
            'isBase64Encoded': True
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"Error: {str(e)}"
        }