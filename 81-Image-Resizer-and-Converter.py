from PIL import Image
import os

def resize_and_convert_image(input_path, output_folder, width, height, output_format="JPEG"):
    os.makedirs(output_folder, exist_ok=True)
    image = Image.open(input_path)
    resized_image = image.resize((width, height))
    
    base_name = os.path.basename(input_path)
    output_path = os.path.join(output_folder, f"{os.path.splitext(base_name)[0]}.{output_format.lower()}")
    
    resized_image.save(output_path, output_format)
    print(f"Image saved at: {output_path}")

input_path = "D:/Github pushed/100-Python-programs-Basic-to-Advanced/mmm.jpeg" 
output_folder = "resized_images"  
resize_and_convert_image(input_path, output_folder, 200, 200, "PNG")
