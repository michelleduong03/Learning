import os
from PIL import Image

def webp_to_jpeg(input_file_path, output_file_path):
    try:
        with Image.open(input_file_path) as img:
            img.convert("RGB").save(output_file_path, format="JPEG")
        print(f"Successfully converted {input_file_path} to {output_file_path}")
    except Exception as e:
        print(f"Error converting image: {e}")

def convert_webp_files(input_directory, output_directory):
    try:
        for filename in os.listdir(input_directory):
            if filename.endswith(".webp"):
                input_file = os.path.join(input_directory, filename)
                output_file = os.path.join(output_directory, filename.replace(".webp", ".jpg"))
                webp_to_jpeg(input_file, output_file)
        print("Batch conversion completed.")
    except Exception as e:
        print(f"Error during batch conversion: {e}")

if __name__ == "__main__":
    input_dir = "images"  
    output_dir = "jpegs" 

    os.makedirs(output_dir, exist_ok=True)

    convert_webp_files(input_dir, output_dir)
