# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 23:36:25 2024

@author: vanev
"""

from PIL import Image # Imports Pillow library for processing images

# ASCII characters used to build text output and display pixel brightness in descending order
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# Resize input image while maintaining aspect ratio
def resize_image(image, new_width=100):
    # Get original dimensions of image
    width, height = image.size
    ratio = height / width / 1.65 # Adjust ratio for better ASCII scaling
    new_height = int(new_width * ratio) # Calculates new height
    resized_image = image.resize((new_width, new_height)) # Resizes and returns image
    return resized_image

# ABSTRACTION: 
# Functions here abstract the key steps of the program (resizing and converting to greyscale)
# Converts resized image to grayscale
def grayify(image):
    grayscale_image = image.convert("L") # "L" converts the image to greyscale
    return grayscale_image

# ALGORITHM: 
#Function implements mapping an algorithm to convert brightness of pixels into separate ASCII levels based on predefined intensity ranges
# Converts greyscale pixels to ASCII characters
def pixels_to_ascii(image):
    pixels = image.getdata() # Obtains pixel intensity values
    characters = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels]) # Maps pixels to ASCII
    return characters

# Main function to convert image to ASCII art
def main(new_width=100):
    # Ask user for image path
    path = input("Enter valid pathname to image:\n").strip() # Prompt for user input for photo location
    try:
        image = Image.open(path) # Attempts to open image
    except FileNotFoundError:
        print(path, "is not a valid pathname to an image.") # If image is not found display error message
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}") # Error message 
        return

    # Resizes, grayifys, and converts image to ASCII
    resized_image = resize_image(image, new_width)
    grayscale_image = grayify(resized_image)
    new_image_data = pixels_to_ascii(grayscale_image)

    # Format ASCII characters into lines that match image width
    pixel_count = len(new_image_data)
    ascii_image = "\n".join(
        new_image_data[i:i + new_width] for i in range(0, pixel_count, new_width)
    )

    # Print final ASCII image result
    print(ascii_image)

    # Save the result to "ascii_image.txt" for text file
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)

# Entry point for program
if __name__ == "__main__":
    main()