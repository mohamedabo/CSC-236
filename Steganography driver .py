######################################################################
# Author: Abdirahman Mohamed  ****** CHANGE THIS!! ******
# username: mohameda ****** CHANGE THIS!! *****

##   Lab L1: Steganography
##   Your names: Abdirahman Mohamed
##   Contributions: Abdirahman Mohamed
##   Purpose: Hides a message in an image then decode it.
##   Acknowledgments: Alexander Smith, Dave Bell and Mario Nakazawa - All helped with debugging
######################################################################
# Acknowledgements:
    # Ben Stephenson: http://pages.cpsc.ucalgary.ca/~jacobs/Courses/cpsc217/W10/code/Topic7/ppm.py
    # working from a class: http://bytes.com/topic/python/answers/520360-trouble-displaying-image-tkinter

#   Modified from code written by Dr. Jan Pearce
#   Modified by Mario Nakazawa, convert to run in Python 3.X. Commented references to tkinter which broke.
#   Original code downloaded from:
#   http://cs.berea.edu/csc226/tasks/yourusername-L3-ppm.py and
#   http://cs.berea.edu/csc226/tasks/ppm.py
######################################################################

import time
from mohameda_csc236L1_ppm import *
# Be sure you work with a single ppm object at a time

def main():
    # The following interaction is just for testing.  You will improve this.

    wn = PPM_set_up()  # To use the PPM class, this must appear at the beginning of your program: send to the initialzer.

    print("\nWelcome to the PPM introduction!\n")

    #ppmdefault=PPM(wn) # uses default file
    #ppmdefault.PPM_display()
    #print("---")

    n=input("Please input name of PPM-P3 file: ")
    #ppmobject=PPM(wn, filename)
    #ppmobject.PPM_make_red()
    #ppmobjecttwo = PPM(wn,filename)
    #ppmobjecttwo.PPM_greyscale()
   # ppmobjecttwo.PPM_flip_horizontal()
   # ppmobjecttwo.PPM_rotateclockwise()
    ppmobjectthree = PPM(wn,n) # object of ppm class
    ppmobjectthree.stringtoaschii()
    ppmobjectthree.PPM_encode_image()
    ppobjectfour = PPM(wn,'mohameda_csc236L1_image-asc.ppm')
    ppobjectfour.PPM_decoded_image()


    #ppmobjectfour.PPM_decoded_image(newval)
    #ppmobject.PPM_display()
    #ppmobjecttwo.PPM_display()
    ppmobjectthree.PPM_display()
    ppobjectfour.PPM_display()


    ppmobjectthree.outasciifile = "mohameda_csc236L1_image.ppm" # the encoded image
    ppobjectfour.outbinfile = "mohameda_csc236L1_image-bin.ppm"

    #ppmtestlist.PPM_display()



    print("\nPush the Quit button to exit all files.")

    #PPM_render(wn) # needed to render all of the images you have instantiated

main()
