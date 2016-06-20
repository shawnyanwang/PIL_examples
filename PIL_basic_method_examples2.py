
'''
PIL_exmaples1

Image.getbands()
Returns a tuple containing the name of each band in this image. For example, getbands on an RGB image returns ("R", "G", "B").

Returns:	A tuple containing band names.
Return type:	tuple

Image.getbbox()
Calculates the bounding box of the non-zero regions in the image.

Returns:	The bounding box is returned as a 4-tuple defining the left, upper, right, and lower pixel coordinate. If the image is completely empty, this method returns None.
Image.getcolors(maxcolors=256)
Returns a list of colors used in this image.

Parameters:	maxcolors - Maximum number of colors. If this number is exceeded, this method returns None. The default limit is 256 colors.
Returns:	An unsorted list of (count, pixel) values.
Image.getdata(band=None)
Returns the contents of this image as a sequence object containing pixel values. The sequence object is flattened, so that values for line one follow directly after the values of line zero, and so on.

Note that the sequence object returned by this method is an internal PIL data type, which only supports certain sequence operations. To convert it to an ordinary sequence (e.g. for printing), use list(im.getdata()).

Parameters:	band - What band to return. The default is to return all bands. To return a single band, pass in the index value (e.g. 0 to get the "R" band from an "RGB" image).
Returns:	A sequence-like object.
Image.getextrema()
Gets the the minimum and maximum pixel values for each band in the image.

Returns:	For a single-band image, a 2-tuple containing the minimum and maximum pixel value. For a multi-band image, a tuple containing one 2-tuple for each band.
Image.getpalette()
Returns the image palette as a list.

Returns:	A list of color values [r, g, b, ...], or None if the image has no palette.

'''
def PIL_exmaples1():
    from PIL import Image
    im = Image.open('Hillary.jpg')
    # return layers
    print im.layers
    # return bands
    print im.getbands()

    print im.getbbox()

    im1 = im.convert("L")
    print im1.getcolors(maxcolors=256)

    print im.getdata()

    print im.getextrema()

    print im.getpalette()

    print im.getpixel((100,120))

    print len(im.histogram())

    print im.histogram()

    print im.mode, im.size, im.width, im.height, im.info



'''
ImageChops ("Channel Operations") Module
The ImageChops module contains a number of arithmetical image operations, called channel operations ("chops"). These can be used for various purposes, including special effects, image compositions, algorithmic painting, and more.

For more pre-made operations, see ImageOps.

At this time, most channel operations are only implemented for 8-bit images (e.g. "L" and "RGB").

Functions
Most channel operations take one or two image arguments and returns a new image. Unless otherwise noted, the result of a channel operation is always clipped to the range 0 to MAX (which is 255 for all modes supported by the operations in this module).

PIL.ImageChops.add(image1, image2, scale=1.0, offset=0)
Adds two images, dividing the result by scale and adding the offset. If omitted, scale defaults to 1.0, and offset to 0.0.

out = ((image1 + image2) / scale + offset)
Return type:	Image
PIL.ImageChops.add_modulo(image1, image2)
Add two images, without clipping the result.

out = ((image1 + image2) % MAX)
Return type:	Image
PIL.ImageChops.blend(image1, image2, alpha)
Blend images using constant transparency weight. Alias for PIL.Image.Image.blend().

Return type:	Image
PIL.ImageChops.composite(image1, image2, mask)
Create composite using transparency mask. Alias for PIL.Image.Image.composite().

Return type:	Image
PIL.ImageChops.constant(image, value)
Fill a channel with a given grey level.

Return type:	Image
PIL.ImageChops.darker(image1, image2)
Compares the two images, pixel by pixel, and returns a new image containing the darker values.

out = min(image1, image2)
Return type:	Image
PIL.ImageChops.difference(image1, image2)
Returns the absolute value of the pixel-by-pixel difference between the two images.

out = abs(image1 - image2)
Return type:	Image
PIL.ImageChops.duplicate(image)
Copy a channel. Alias for PIL.Image.Image.copy().

Return type:	Image
PIL.ImageChops.invert(image)
Invert an image (channel).

out = MAX - image
Return type:	Image
PIL.ImageChops.lighter(image1, image2)
Compares the two images, pixel by pixel, and returns a new image containing the lighter values.

out = max(image1, image2)
Return type:	Image
PIL.ImageChops.logical_and(image1, image2)
Logical AND between two images.

out = ((image1 and image2) % MAX)
Return type:	Image
PIL.ImageChops.logical_or(image1, image2)
Logical OR between two images.

out = ((image1 or image2) % MAX)
Return type:	Image
PIL.ImageChops.multiply(image1, image2)
Superimposes two images on top of each other.

If you multiply an image with a solid black image, the result is black. If you multiply with a solid white image, the image is unaffected.

out = image1 * image2 / MAX
Return type:	Image
PIL.ImageChops.offset(image, xoffset, yoffset=None)
Returns a copy of the image where data has been offset by the given distances. Data wraps around the edges. If yoffset is omitted, it is assumed to be equal to xoffset.

Parameters:
xoffset -  The horizontal distance.
yoffset - The vertical distance. If omitted, both distances are set to the same value.
Return type:
Image

PIL.ImageChops.screen(image1, image2)
Superimposes two inverted images on top of each other.

out = MAX - ((MAX - image1) * (MAX - image2) / MAX)
Return type:	Image
PIL.ImageChops.subtract(image1, image2, scale=1.0, offset=0)
Subtracts two images, dividing the result by scale and adding the offset. If omitted, scale defaults to 1.0, and offset to 0.0.

out = ((image1 - image2) / scale + offset)
Return type:	Image
PIL.ImageChops.subtract_modulo(image1, image2)
Subtract two images, without clipping the result.

out = ((image1 - image2) % MAX)
Return type:	Image




'''

def PIL_exmaples2():
    import PIL
    from PIL import Image
    image1 = Image.open("apple.jpg")
    image2 = Image.open("background.jpg")
    im = PIL.ImageChops.difference(image1, image2)
    com_im = Image.new('RGB', (image1.width*2, image2.height*2))
    com_im.paste(im, (0,0))
    im = PIL.ImageChops.lighter(image1, image2)
    com_im.paste(im, (image1.width,0))
    im = PIL.ImageChops.multiply(image1, image2)
    com_im.paste(im, (0,image2.height))
    im = PIL.ImageChops.subtract_modulo(image1, image2)
    com_im.paste(im, (image1.width,image2.height))
    com_im.show()




if __name__=='__main__':
    PIL_exmaples2()
