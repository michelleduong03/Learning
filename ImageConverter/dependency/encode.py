import base64

# Path to your image file
image_path = "../images/re_encoded_image.webp"

# Read the image file in binary mode
with open(image_path, 'rb') as img_file:
    image_data = img_file.read()

# Base64 encode the image data
encoded_image = base64.b64encode(image_data)
encoded_image_str = encoded_image.decode('utf-8')

# Write the base64 string to a file
with open('encoded_image.txt', 'w') as output_file:
    output_file.write(encoded_image_str)

print("Base64 encoded string written to 'encoded_image.txt'")

