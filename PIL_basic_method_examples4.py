
def PIL_example1(imname =  'Hillary.jpg'):
    from PIL import Image
    import PIL
    im = Image.open(imname)



    im.show()


if __name__ == '__main__':
    import thread
    import time

    # defined a function for thread
    def print_time( threadName, delay):
       count = 0
       while count < 5:
          time.sleep(delay)
          count += 1
        #   print "%s: %s" % ( threadName, time.ctime(time.time()) )
          print threadName, count

    # created two threads
    try:
        # thread.start_new_thread(PIL_example1, ('Hillary.jpg'))
        # thread.start_new_thread(PIL_example1, ('apple.jpg'))
        thread.start_new_thread( print_time, ("Thread-1", 2, ) )
        thread.start_new_thread( print_time, ("Thread-2", 4, ) )


    except:
       print "Error: unable to start thread"

    while 1:
       pass
