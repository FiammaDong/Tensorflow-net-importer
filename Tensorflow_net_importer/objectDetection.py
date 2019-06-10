#!/usr/bin/env python
import cv2

# Load a model imported from Tensorflowload using OpenCV dnn module
cvNet = cv2.dnn.readNetFromTensorflow('/home/del22/DeepLearning/ComputerVision/Tensorflow_net_importer/frozen_inference_graph.pb', '/home/del22/DeepLearning/ComputerVision/Tensorflow_net_importer/graph.pbtxt')

# Input image
img = cv2.imread("/home/del22/DeepLearning/ComputerVision/Tensorflow_net_importer/img2.jpg")
rows = img.shape[0]
cols = img.shape[1]

# Use the given image as input, which needs to be blob(s).
cvNet.setInput(cv2.dnn.blobFromImage(img, size=(300, 300), swapRB=True, crop=False))

# Runs a forward pass to compute the net output
cvOut = cvNet.forward()

# Loop on the outputs
for detection in cvOut[0,0,:,:]:
    score = float(detection[2])
    if score > 0.3:
        left = detection[3] * cols
        top = detection[4] * rows
        right = detection[5] * cols
        bottom = detection[6] * rows
        cv2.rectangle(img, (int(left), int(top)), (int(right), int(bottom)), (23, 230, 210), thickness=2)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
