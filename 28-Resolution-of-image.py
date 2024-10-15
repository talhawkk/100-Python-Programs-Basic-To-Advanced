#python program to find resolution of image
import PIL
from PIL import Image
img=PIL.Image.open("C:/Users/Talha/Desktop/Python/tt.png")
w,l=img.size
print(w,l)