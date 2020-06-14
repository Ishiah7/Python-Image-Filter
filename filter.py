from PIL import Image, ImageFilter
import sys

# Gets User Input
print("IMAGE FILTER\n")
print("Filters:")
print("BLUR, FIND_EDGES, EDGE_ENHANCE, SHARPEN, CONTOUR\n")

while True:
    mode = input("Enter Filter Name: ")
    if len(mode) > 0:
        break

while True:
    imageInput = input("Enter Input Image Filepath: ")
    if len(imageInput) > 0:
        break

while True:
    outputName = input("Enter Output Image Name: ")
    if len(outputName) > 0:
        break


# Opens Image Given By User
# If User Image Can't Open,Error Message Is Printed
try:
    originalImage = Image.open(imageInput)
except:
    print("Unable to open image")


# Cases For Each Of The Filters
if mode.lower() == "blur":
    outputImage = originalImage.filter(ImageFilter.GaussianBlur(radius=20))
    outputImage.show()
if mode.lower() == "find_edges":
    outputImage = originalImage.filter(ImageFilter.FIND_EDGES)
    outputImage.show()
if mode.lower() == "sharpen":
    outputImage = originalImage.filter(ImageFilter.SHARPEN)
    outputImage.show()
if mode.lower() == "edge_enhance":
    outputImage = originalImage.filter(ImageFilter.EDGE_ENHANCE)
    outputImage.show()
if mode.lower() == "contour":
    outputImage = originalImage.filter(ImageFilter.CONTOUR)
    outputImage.show()


# Opens The Output Image So User Can See
imageformat = originalImage.format

# Creates A New Image File WIth The Ouput Image
outputImage.save(f"{outputName}." + f"{imageformat.lower()}")
