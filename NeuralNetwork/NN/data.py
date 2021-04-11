#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 01:36:47 2021

@author: llabori
"""

import numpy as ny
import pathlib

def get_mnist():
    with ny.load(f"{pathlib.Path(__file__).parent.absolute()}/data/mnist.npz") as f:
        images, labels = f["x_train"], f["y_train"]
    images = images.astype("float32") / 255.0
    images = ny.reshape(images, (images.shape[0], images.shape[1] * images.shape[2]))
    labels = ny.eye(10)[labels]
    return images, labels