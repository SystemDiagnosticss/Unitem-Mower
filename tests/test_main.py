
import pytest
import cv2
import numpy as np
from main import img_saver, img_operation, producer, consumer, DECREASER

def test_img_saver_empty_queue():
    with pytest.raises(TypeError):
        img_saver()

def test_save_images_empty_image():
        h = 100
        w = 100
        new_image = np.zeros((h,w,3), np.uint8)
        img = img_operation(new_image)
        height, width = img.shape[:2]
        assert height == h/DECREASER, width == w/DECREASER