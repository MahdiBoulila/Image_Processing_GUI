#
# Final Project
#
# Sarah Foley and Mahdi Boulila
#
# 

from cs120png import *
import tkinter as tk

def finder(image1, image2):
    """ loads 2 PNG image from the file with the specified filenames
        
        input: 
        image1, string: the global image
        image2, string: the cropped image
                
        If it has successfully finded image2 in image1, then
        it would return the coordinates of where image2 stars in image1
        If not, it would return the message 'Not Found'
    """
    # create an image object for the image stored in 
    # file1 with the specified filename
    img1 = load_image(image1)

    # determine the dimensions of the image
    height1 = img1.get_height()
    width1 = img1.get_width()

    # create an image object for the image stored in
    # file2 with the specified filename
    img2 = load_image(image2)

    # determine the dimensions of the image
    height2 = img2.get_height()
    width2 = img2.get_width()

    # process the image, one pixel at a time
    rgb_img2_0 = img2.get_pixel(0,0) 
    for row1 in range(height1-height2+1):
        for col1 in range(width1-width2+1):
            # get the RGB values of the pixel at row r, column c
            rgb_img1 = img1.get_pixel(row1, col1)    
            # if the first pixel matches, then start looking for image2
            if rgb_img1 == rgb_img2_0:
                test_same = compare(img1, img2, row1, col1)
                # if we found the image
                if test_same:
                    # Save a highlighted version of the image, and return
                    # the coordinates
                    highlight(img1, row1, col1, height1, width1, height2, width2 )
                    tk.messagebox.showinfo(title='Done', message='The program has successfully found the cropped image in the global image')
                    return [row1,col1]

    # Else, return this message
    tk.messagebox.showinfo(title='Oops', message='Could not find the cropped image in the global image')
    return 'Not Found'



def compare(img1, img2, rmin1, cmin1):  ###helper fucntion####
    """
    says if the second image is in the original image 

    input img1: PNG image file
    input img2: PNG image file
    input rmin1: number
    input rmax1: number
    """
    height2 = img2.get_height()
    width2 = img2.get_width()
    # process the image, one pixel at a time
    for r in range(height2): #for r in range(rmin, rmax)
        for c in range(width2):
            row1 = r + rmin1
            col1 = c + cmin1
            
            # get the RGB values of the pixel at row r, column c
            rgb1 = img1.get_pixel(row1, col1)
            rgb2 = img2.get_pixel(r, c)
            # print(rgb1,rgb2)
            if rgb1 != rgb2:
                return False
    return True             



def highlight(img1, rmin2, cmin2, height1, width1, height2, width2 ):
    """
    loads the PNG image files with the specified filename and highlights 
    the part of the org. image that the  second image is in that is specified 
    by the other four parameters (that are from the smaller image).

    input img1: PNG image file
    input rmin1: number
    input rmax1: number
    """

    # create new image
    new_img = Image(height1, width1)   # new, blank image object that is the size of image 1
    # copy image1 to new_img
    for row in range(height1):
        for col in range(width1):
            rgb = img1.get_pixel(row, col)
            new_img.set_pixel(row, col, rgb)

    rmax2 = rmin2 + height2
    cmax2 = cmin2 + width2
    # process the image, one pixel at a time
    for r in range(rmin2, rmax2):
        for c in range(cmin2, cmax2):
            # get the RGB values of the pixel at row r, column c
            rgb = img1.get_pixel(r, c)  #get og image           
            red = rgb[0]
            green = rgb[1]
            blue = rgb[2]

            #create a ratio to decrease blue and green values
            new_green = int(green * .5)
            new_blue = int(blue * .5)

            #give new color values
            new_rgb = [red, new_green, new_blue] #list
            new_img.set_pixel(r, c, new_rgb) 

    # save the modified image, using a filename that is based on the
    # name of the original file.
    new_filename = 'result.png'
    new_img.save(new_filename)




    
