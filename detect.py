import numpy as np
import pandas as pd 
import torch
import torch.nn as nn
import cv2
import os
import time
from torch.autograd import Variable
import matplotlib.pyplot as plt

weightsfile = ''
classfile = ''
cfgfile = ''
sample_img1 = ''
input_dir = ''
output_dir = ''
nms_thesh = 0.5