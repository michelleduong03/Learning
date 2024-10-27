# import requests

# url = "https://0au0qyekq0.execute-api.us-west-2.amazonaws.com/dev/convert"
# image_path = "../images/ap.webp"
# with open(image_path, 'rb') as img_file:
#     # Proceed with the file operation (like uploading to API)
#     response = requests.post(url, files={'image': img_file})

# # response = requests.post(url, files=files)

# print(response.status_code)
# print(response.json())  # or response.content for raw data
# import requests
# import base64

# url = "https://0au0qyekq0.execute-api.us-west-2.amazonaws.com/dev/convert"
# image_path = "../images/ap.webp"

# # Read the image file and encode it to base64
# with open(image_path, 'rb') as img_file:
#     image_data = img_file.read()
#     image_base64 = base64.b64encode(image_data).decode('utf-8')

# # Send the POST request with Base64 image data
# response = requests.post(url, json={"body": image_base64})

# print(response.status_code)
# if response.status_code == 200:
#     # If the response contains an image, you can decode it
#     image_output_base64 = response.json()['body']
#     image_output = base64.b64decode(image_output_base64)
#     with open('converted_image.jpg', 'wb') as output_file:
#         output_file.write(image_output)
# else:
#     print(response.text)
# import os
# from PIL import Image

# # Path to the image file
# image_path = "../images/ap.webp"

# # Function to open and save the image
# def open_and_save_image(file_path):
#     try:
#         # Open the image using Pillow
#         img = Image.open(file_path)
        
#         # Print image details
#         print(f"Format: {img.format}")
#         print(f"Size: {img.size}")
#         print(f"Mode: {img.mode}")
        
#         # Save the image again to re-encode it
#         re_encoded_path = os.path.join(os.path.dirname(file_path), "re_encoded_image.webp")
#         img.save(re_encoded_path, "WEBP")  # Save it back as WebP or change to "PNG"
#         print(f"Image saved successfully as {re_encoded_path}")

#     except Exception as e:
#         print(f"Error opening or saving image: {e}")

# # Main script execution
# if __name__ == "__main__":
#     open_and_save_image(image_path)
import requests

# Define the URL of your API endpoint
url = "https://0au0qyekq0.execute-api.us-west-2.amazonaws.com/dev/convert"

# Path to the image file you want to send
image_path = "../images/re_encoded_image.webp"  # Adjust the path as necessary

try:
    # Open the image file in binary mode
    with open(image_path, 'rb') as img_file:
        # Send a POST request to the API
        response = requests.post(url, files={'image': img_file})

    # Check the status code and print the response
    print("Status Code:", response.status_code)

    # Print the response content
    if response.status_code == 200:
        print("Response JSON:", response.json())
    else:
        print("Response Content:", response.content)

except FileNotFoundError:
    print(f"Error: The file '{image_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")



