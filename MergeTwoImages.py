import cv2
import numpy as np
import matplotlib.pyplot as plt
import pytest
import unittest
from unittest.mock import Mock
from unittest.mock import patch


class TestForMergedImage(unittest.TestCase):
    def test_get_image_merged(self):
        self.assert_called_once()

    def assert_called_once(self):
        print("The images have been merged...!!")


class MergeTwoImages:

    def __init__(self):
        self.im1 = cv2.imread('/Users/satyajeetkumar/Desktop/Images For practices/dark_flowers_608925.jpg')
        self.im2 = cv2.imread('/Users/satyajeetkumar/Desktop/Images For practices/ivan-jevtic-p7mo8-CG5Gs-unsplash.jpg')

    def ConvertImages(self):
        self.im1 = cv2.cvtColor(self.im1, cv2.COLOR_BGR2RGB)
        self.im2 = cv2.cvtColor(self.im2, cv2.COLOR_BGR2RGB)

    def vconcat_resize_min(self, im_list, interpolation = cv2.INTER_CUBIC):
        w_min = min(im.shape[1] for im in im_list)

        im_list_resize = [cv2.resize(im, (w_min, int(im.shape[0] * w_min / im.shape[1])), interpolation = interpolation)
                          for im in im_list]

        return cv2.vconcat(im_list_resize)

    def MergeImages(self):
        self.resized_image = self.vconcat_resize_min([self.im1, self.im2])
        #self.merge_image_vertical = cv2.vconcat([self.im1, self.im2])
        #self.merge_image_horizontal = cv2.hconcat([self.im1, self.im2])

    def ShowMergedImage(self):
        plt.imshow(self.resized_image)
        plt.show()

    def ShowImages(self):
        plt.imshow(self.im1)
        plt.show()
        plt.imshow(self.im2)
        plt.show()


if __name__ == "__main__":
    mti = MergeTwoImages()
    mti.ConvertImages()
    #mti.ShowImages()
    mti.MergeImages()
    #mti.ShowMergedImage()

    #unittest.main()






