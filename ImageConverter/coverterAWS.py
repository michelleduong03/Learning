import os
import boto3
from PIL import Image

s3 = boto3.client('s3')

def jpeg_to_png(input_file_path, output_file_path):
    try:
        with Image.open(input_file_path) as img:
            img.save(output_file_path, format="PNG")
        print(f"Successfully converted {input_file_path} to {output_file_path}")
    except Exception as e:
        print(f"Error converting image: {e}")
        raise e

def lambda_handler(event, context):
    # Extract bucket name and object key from the S3 event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    jpeg_file_key = event['Records'][0]['s3']['object']['key']
    
    # Define the local path for temporary storage
    input_file = f"/tmp/{os.path.basename(jpeg_file_key)}"
    output_file = f"/tmp/{os.path.basename(jpeg_file_key).rsplit('.', 1)[0]}.png"

    # Download the JPEG file from S3
    s3.download_file(bucket_name, jpeg_file_key, input_file)

    # Convert JPEG to PNG
    jpeg_to_png(input_file, output_file)

    # Define the output file key
    png_file_key = jpeg_file_key.rsplit('.', 1)[0] + '.png'
    
    # Upload the PNG file back to S3
    s3.upload_file(output_file, bucket_name, png_file_key)

    return {
        "statusCode": 200,
        "body": f"Successfully converted {jpeg_file_key} to {png_file_key}"
    }
