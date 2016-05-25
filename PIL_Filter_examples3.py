
'''
1.GaussianBlur_fiter, UnsharpMask, Kernel


class PIL.ImageFilter.GaussianBlur(radius=2)
Gaussian blur filter.

Parameters: radius - Blur radius.


class PIL.ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3)
Unsharp mask filter.

See Wikipedia's entry on digital unsharp masking for an explanation of the parameters.

Parameters:
radius- Blur Radius
percent-Unsharp strength, in percent
threshold-Threshold controls the minimum brightness change that will be sharpened


class PIL.ImageFilter.Kernel(size, kernel, scale=None, offset=0)
Create a convolution kernel. The current version only supports 3x3 and 5x5 integer and floating point kernels.

In the current version, kernels can only be applied to "L" and "RGB" images.

Parameters:
size- Kernel size, given as (width, height). In the current version, this must be (3,3) or (5,5).
kernel-A sequence containing kernel weights.
scale-Scale factor. If given, the result for each pixel is divided by this value. the default is the sum of the kernel weights.
offset-Offset. If given, this value is added to the result, after it has been divided by the scale factor.
'''

def fiter_example1():
    from PIL import Image
    from PIL import ImageFilter
    sourceFileName = "Hillary.jpg"
    # Open image
    img = Image.open(sourceFileName)
    # copy image
    img1 = img.copy()
    # Gaussian blur filtering  ######################################################
    img1 = img1.filter(ImageFilter.GaussianBlur(radius = 2))
    # create new image object
    combine_imag = Image.new("RGB", [img.size[0]*2,img.size[1]*2])
    # fill original image and processing image in the combine image
    combine_imag.paste(img,(0,0))
    combine_imag.paste(img1,(0,img.size[1]))
    # UnsharpMask fiter  ######################################################
    img1 = img.filter(ImageFilter.UnsharpMask(radius=2, percent=100, threshold=3))
    combine_imag.paste(img1,(img.size[0],0))
    # Kernel filter ######################################################
    img1 = img.filter(ImageFilter.Kernel(size = (3,3), kernel = (-1,-1,-1,-1,8,-1,-1,-1,-1), scale=None, offset=0))
    combine_imag.paste(img1,(img.size[0], img.size[1]))
    # show image
    combine_imag.show()
    # print  help(ImageFilter)
'''
2. RankFilter(include median filter), MedianFilter, MinFilter


class PIL.ImageFilter.RankFilter(size, rank)
Create a rank filter. The rank filter sorts all pixels in a window of the given size, and returns the rank'th value.

Parameters:
size-The kernel size, in pixels.
rank-What pixel value to pick. Use 0 for a min filter, size * size / 2 for a median filter, size * size - 1 for a max filter, etc.

class PIL.ImageFilter.MedianFilter(size=3)
Create a median filter. Picks the median pixel value in a window with the given size.

Parameters:	size-The kernel size, in pixels.


class PIL.ImageFilter.MinFilter(size=3)
Create a min filter. Picks the lowest pixel value in a window with the given size.

Parameters:	size-The kernel size, in pixels.



'''
def fiter_example2():
    from PIL import Image
    from PIL import ImageFilter
    sourceFileName = "Hillary.jpg"
    # Open image
    img = Image.open(sourceFileName)
    # copy image
    img1 = img.copy()
    # RankFilter filtering  ######################################################
    img1 = img1.filter(ImageFilter.RankFilter(3,7))
    # create new image object
    combine_imag = Image.new("RGB", [img.size[0]*2,img.size[1]*2])
    # fill original image and processing image in the combine image
    combine_imag.paste(img,(0,0))
    combine_imag.paste(img1,(0,img.size[1]))
    # MedianFilter fiter  ######################################################
    img1 = img.filter(ImageFilter.MedianFilter(3))
    combine_imag.paste(img1,(img.size[0],0))
    # MinFilterl filter
    img1 = img.filter(ImageFilter.MinFilter(3))
    combine_imag.paste(img1,(img.size[0], img.size[1]))
    # show image
    combine_imag.show()
    #
'''
3.MaxFilter, ModeFilter

class PIL.ImageFilter.MaxFilter(size=3)
Create a max filter. Picks the largest pixel value in a window with the given size.

Parameters:	size - The kernel size, in pixels.


class PIL.ImageFilter.ModeFilter(size=3)
Create a mode filter. Picks the most frequent pixel value in a box with the given size. Pixel values that occur only once or twice are ignored; if no pixel value occurs more than twice, the original pixel value is preserved.

Parameters:	size - The kernel size, in pixels.

'''

def fiter_example3():
    from PIL import Image
    from PIL import ImageFilter
    sourceFileName = "Hillary.jpg"
    # Open image
    img = Image.open(sourceFileName)
    # copy image
    img1 = img.copy()
    # MaxFilter  ######################################################
    img1 = img1.filter(ImageFilter.MaxFilter(3))
    # create new image object
    combine_imag = Image.new("RGB", [img.size[0]*2,img.size[1]*2])
    # fill original image and processing image in the combine image
    combine_imag.paste(img,(0,0))
    combine_imag.paste(img1,(0,img.size[1]))
    # ModeFilter  ######################################################
    img1 = img.filter(ImageFilter.ModeFilter(3))
    combine_imag.paste(img1,(img.size[0],0))
    # BLUR filter
    img1 = img.filter(ImageFilter.BLUR)
    combine_imag.paste(img1,(img.size[0], img.size[1]))
    # show image
    combine_imag.show()


if __name__=="__main__":
    from PIL import ImageFilter
    print  help(ImageFilter)

    fiter_example3()
