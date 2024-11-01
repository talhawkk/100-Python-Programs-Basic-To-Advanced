from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGB', (600, 200), color='white')

draw = ImageDraw.Draw(img)
try:
    #enter path of font file with .ttf extenshion here:
    font_path = "D:/Github pushed/Convert-Text-To-Handwriting/Caveat-VariableFont_wght.ttf"  
    font = ImageFont.truetype("Caveat-VariableFont_wght.ttf", 40)

    text=input("Enter Test that you want to convert into hanwriting : ")

    draw.text((10, 50), text, font=font, fill=(0, 0, 0))
    img.save("handwritten_text.png")
except Exception as e:
    print(f"Error occured : {e}")
