import os
import argparse
from skimage.metrics import structural_similarity
import imutils
import cv2
import hashlib

# get the image size through os liberary using getsize function
def ImSize(image):
    try:
        size = os.path.getsize(image)
    except Exception as e:
        print(e)
    return size

 # hashing the files using MD5 hash function
def ImHash(file):
    with open(file, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()


# system arguement to (ask the client entering the images)
arg = argparse.ArgumentParser()
arg.add_argument("-i", "--image1", required=True,help="the first image")
arg.add_argument("-j", "--image2", required=True,help="the second image")
args = vars(arg.parse_args())



# Delegating tasks to other functions ( Pass the images on the two functions "hashing and size function", and then store the data in the new defined functions size, size2 and hash ,hash2)
size = ImSize(args["image1"])
hash = ImHash(args["image1"])
size2 = ImSize(args["image2"])
hash2 = ImHash(args["image2"])
print(args["image1"], '\t', 'size: ',size, '\t', 'Hash: ', hash)
print(args["image2"], '\t', 'size: ',size2, '\t', 'Hash: ', hash2)

# load the two input images and reading them
imageA = cv2.imread(args["image1"])
imageB = cv2.imread(args["image2"])
 
# convert the images to grayscale
grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

# check their similarty
(score, diff) = structural_similarity(grayA, grayB, full=True)
diff = (diff * 255).astype("uint8")
print("Structural Similarty: {}".format(score))
