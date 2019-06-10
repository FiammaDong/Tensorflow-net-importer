# Tensorflow-net-importer

How to load Tensorflow models with OpenCV:

A very useful functionality was added to OpenCV’s DNN module: a Tensorflow net importer.
To use the DNN, the opencv_contrib is needed, make sure to install it.

"cv2.dnn.readNetFromTensorflow('frozen_inference_graph.pb', 'graph.pbtxt')"
Two files are needed: ".pb" and ".pbtxt"
OpenCV requires an extra configuration file based on the .pb, the  .pbtxt. It is possible to 
import your own models and generate your own .pbtxt files by using one of the following files from the OpenCV Github repository.

tf_text_graph_ssd.py
tf_text_graph_common.py
tf_text_graph_faster_rcnn.py
tf_text_graph_mask_rcnn.py

Change the path to ".pb", ".pbtxt", and to the input image in "objectDetection.py" file and run it.

Test Images:
![img2](https://user-images.githubusercontent.com/7738407/59230479-93fcd680-8bab-11e9-8175-9af1a963543b.jpg)
![img](https://user-images.githubusercontent.com/7738407/59230476-90694f80-8bab-11e9-90eb-0d95397fa969.jpg)
![img1](https://user-images.githubusercontent.com/7738407/59230477-92331300-8bab-11e9-98b5-be340069f05b.jpg)

Resultant Images:
![resImg1](https://user-images.githubusercontent.com/7738407/59230386-4f713b00-8bab-11e9-8bf1-aa9a0a7ac295.jpg)
![resImg2](https://user-images.githubusercontent.com/7738407/59230426-73348100-8bab-11e9-9f73-d95218c7c2f5.jpg)
![resImg3](https://user-images.githubusercontent.com/7738407/59230433-74fe4480-8bab-11e9-9d85-7ba512a6c571.jpg)
