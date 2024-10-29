import io
import boto3
from PIL import Image
import base64

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    try:
        # Get the base64 image from the event body
        body = json.loads(event['body'])
        base64_image = body['body']
        
        # Decode the base64 image
        image_data = base64.b64decode(base64_image)

        # Convert the WEBP image to JPEG
        input_image = Image.open(io.BytesIO(image_data))
        output_image_io = io.BytesIO()
        input_image.convert("RGB").save(output_image_io, format="JPEG")
        output_image_io.seek(0)

        # Save the converted image back to S3
        output_key = f'converted_image_{context.aws_request_id}.jpg'
        s3_client.put_object(
            Bucket='your-s3-bucket-name',  # Replace with your bucket name
            Key=output_key,
            Body=output_image_io,
            ContentType='image/jpeg'
        )

        return {
            'statusCode': 200,
            'body': f'Successfully converted and saved to {output_key}'
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"Error: {str(e)}"
        }
