
# 1.Open, rotate, and display an image (using the default viewer)
def example1():
    from PIL import Image
    sourceFileName = "Luf.jpg"
    I = Image.open(sourceFileName)
    I.show()
    I.rotate(30).show()

# 2. Create thumbnails
def example2():
    from PIL import Image
    import glob, os

    size = 32, 32

    for infile in glob.glob("*.jpg"):
        # The glob module finds all the pathnames matching a specified pattern according to the rules used by the Unix shell
        file, ext = os.path.splitext(infile)
        im = Image.open(infile)
        I = im.thumbnail(size)
        im.save(file + ".thumbnail", "JPEG")

# 3.Image.alpha_composite
def example3():
    from PIL import Image
    im1 = Image.open('apple.jpg').convert("RGBA")
    im1.putalpha(256) # set alpha to given value
    im2 = Image.open('background.jpg').convert("RGBA")
    im2.putalpha(100)
    # mask = Image.new('L', (700, 800), 0)
    I = Image.alpha_composite(im1,im2)
    I.show()
# 4.PIL.Image.blend(im1, im2, alpha)
# Creates a new image by interpolating between two input images, using a constant alpha.:
#
#     out = image1 * (1.0 - alpha) + image2 * alpha

def example4():
    from PIL import Image
    im1 = Image.open('apple.jpg').convert("RGBA")
    im2 = Image.open('background.jpg').convert("RGBA")
    I = Image.blend(im1,im2,0.2)
    I.show()

# 5.PIL.Image.composite(image1, image2, mask)
# Create composite image by blending images using a transparency mask.

def example5():
    from PIL import Image
    im1 = Image.open('apple.jpg').convert("RGBA")
    im2 = Image.open('background.jpg').convert("RGBA")
    mask = Image.new('L', (700, 800), 128)
    I = Image.composite(im1,im2,mask)
    I.show()

# 6.PIL.Image.eval(image, *args)
# Applies the function (which should take one argument) to each pixel in the given
# image. If the image has more than one band, the same function is applied to each band.
# Note that the function is evaluated once for each possible pixel value, so you cannot
# use random components or other generators.
def example6():
    from PIL import Image
    f = lambda x: x*1.5
    sourceFileName = "Hillary.jpg"
    I = Image.open(sourceFileName)
    I = Image.eval(I, f)
    I.show()

# 7.PIL.Image.merge(mode, bands)
# Merge a set of single band images into a new multiband image.
    # Parameters:
    # mode-The mode to use for the output image. See: Modes.
    # bands-A sequence containing one single-band image for each band in the output image. All bands must have the same size.
    # Returns:
    # An Image object.
def example7():
    from PIL import Image
    sourceFileName = "Hillary.jpg"
    # im1 = Image.open('apple.jpg')
    # im2 = Image.open('background.jpg')
    I = Image.open(sourceFileName)
    I = Image.merge('HSV', I.split())
    print I.split()
    I.show()

# the following standard modes:
#
# 1 (1-bit pixels, black and white, stored with one pixel per byte)
# L (8-bit pixels, black and white)
# P (8-bit pixels, mapped to any other mode using a color palette)
# RGB (3x8-bit pixels, true color)
# RGBA (4x8-bit pixels, true color with transparency mask)
# CMYK (4x8-bit pixels, color separation)
# YCbCr (3x8-bit pixels, color video format)
# Note that this refers to the JPEG, and not the ITU-R BT.2020, standard
# LAB (3x8-bit pixels, the L*a*b color space)
# HSV (3x8-bit pixels, Hue, Saturation, Value color space)
# I (32-bit signed integer pixels)
# F (32-bit floating point pixels)

# 8.Constructing images
# PIL.Image.new(mode, size, color=0)
def example8():
    from PIL import Image
    I = Image.new('1', (700, 800), 0)
    I.show()

# 9.PIL.Image.fromarray(obj, mode=None)
# Creates an image memory from an object exporting the array interface (using the buffer protocol).
#
# If obj is not contiguous, then the tobytes method is called and frombuffer() is used.
def example9():
    from PIL import Image
    from numpy import eye
    arr = (eye(200)*255).astype('uint8') # sample array
    im = Image.fromarray(arr).convert('RGB')
    im.show()

# 10.PIL.Image.frombytes(mode, size, data, decoder_name='raw', *args)
# Creates a copy of an image memory from pixel data in a buffer.
#
# In its simplest form, this function takes three arguments (mode, size, and unpacked pixel data).
#
# You can also use any pixel decoder supported by PIL. For more information on available decoders, see the section Writing Your Own File Decoder.
#
# Note that this function decodes pixel data only, not entire images. If you have an entire image in a string, wrap it in a BytesIO object, and use
def example10():
    from PIL import Image
    sourceFileName = "Hillary.jpg"
    img = Image.open(sourceFileName)
    raw = img.tobytes()
    f = open('output', 'wb')
    f.write(raw)
    f.close()
    # print raw
    img2 = Image.frombytes(img.mode, img.size, byte)
    im2.show()
# 11.Image.copy() and Image.crop(box=None)
# Image.crop(box=None)
# Returns a rectangular region from this image. The box is a 4-tuple defining the left, upper, right, and lower pixel coordinate.
#
# This is a lazy operation. Changes to the source image may or may not be reflected in the cropped image. To break the connection, call the load() method on the cropped copy.
def example11():
    from PIL import Image
    sourceFileName = "Hillary.jpg"
    img = Image.open(sourceFileName)
    img1 = img.crop(box=(100,100,500,200))
    img2 = img1.copy()
    img2.show()
# 12.Image.draft(mode, size)
# Configures the image file loader so it returns a version of the image that as closely as possible matches the given mode and size. For example, you can use this method to convert a color JPEG to greyscale while loading it, or to extract a 128x192 version from a PCD file.
#
# Note that this method modifies the Image object in place. If the image has already been loaded, this method has no effect.
def example12():
    from PIL import Image
    sourceFileName = "Hillary.jpg"
    img = Image.open(sourceFileName)
    img.draft('1',(1000,800))
    img.show()

if __name__=='__main__':
    example12()
