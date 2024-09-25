import numpy as np
import pandas as pd 
import torch
import torch.nn as nn
import cv2
import os
import time
from torch.autograd import Variable
import matplotlib.pyplot as plt

weightsfile = '/home/mittesh/Downloads/Datasets/yolo_v3_dataset_weights_file/yolov3.weights'
classfile = 'yolo_v3_kernel_datatset/Input/coco.names'
cfgfile = 'yolo_v3_kernel_datatset/Input/yolov3.cfg'
sample_img1 = 'yolo_v3_kernel_datatset/Input/dog.jpg'
input_dir = 'Object-detection/yolo_v3_kernel_datatset/Input'
output_dir = 'Object-detection/yolo_v3_kernel_datatset/Output'
nms_thesh = 0.5