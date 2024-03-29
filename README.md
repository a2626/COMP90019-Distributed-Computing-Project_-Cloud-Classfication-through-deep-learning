# COMP90019-Distributed-Computing-Project_-Cloud-Classfication-through-deep-learning

# Project Title: Cloud Classification through Deep Learning
In this project, our goal is to use deep learning to detect the type of clouds on the images. Currently, there are ten type of clouds in the sky, as following.
1. cirrocumulus
2. cirrostratus
3. cirrus
4. cumulonimbus
5. altocumulus
6. altostratus
7. cumulus
8. nimbostratus
9. stratocumulus
10. lenticularis
# Project Structure
* img_collection folder: One python script used to collect images from Google and Baidu. Two txt files contain the name of different clouds in English and Chinese separately.
* img_processing folder: Three python scripts, Encoding_Checker.py is used to check the jpg files that contains png encoding. corrupted_Checker.py is used to check whether images been seen properly or not. ResizeImage.py is used to change the size of images to under 300kb.
* Object Detection TEST: I use this script to test my model locally.
* Configuration: it contains all my models parameter.
* web_application: I use this to demo my model.

# System Environment
* OS: macOS 10.14.4
* RAM: 16GB
* CPU: Intel Core i7 2.6GHz
* GPU: Radeon Pro 450 2GB and Intel HD Graphics 530 1536 MB

# Project Steps
1. Install TensorFlow GPU or CPU version and the releated package. The more detailed can be found at https://github.com/tensorflow/tensorflow

2. Install TensorFlow Object Detection API. The more detailed can be found at https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md

3. Labelling images with LabelImg. The more detailed can be found at https://github.com/tzutalin/labelImg

4. Prepare TFRecord

5. Training through TensorFlow model zoo. The more detailed can be found at
https://github.com/tensorflow/models Also, the new version of meta-architecture can be found at https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md

6. Testing with TensorBoard

7. Optimization 

8. Export final model and implemented on Google Cloud to build a website
