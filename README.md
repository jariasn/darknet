![Project Logo](https://drive.google.com/uc?id=1ETWP_aKZDNQQAPC8MeBEC9jGH4u8Vqfz)

# Duckiebot Object Detection with YOLO v3

This project focuses on the training and implementation of YOLO v3 in a Duckiebot for real-time object detection. The goal is to identify and classify objects such as Duckiebots, Ducks, Road signs, and Stop signs.

## Darknet 
Darknet is an open source neural network framework written in C and CUDA. It is fast, easy to install, and supports CPU and GPU computation.

## Getting Started

### Cloning the Darknet Repository

Clone the Darknet repository from [https://github.com/pjreddie/darknet.git](https://github.com/pjreddie/darknet.git) by running the following command:

```bash
git clone https://github.com/pjreddie/darknet.git
```
### Creating the Dataset
To train the model, create the dataset by collecting images of Ducktown and taking your own images. Use a Laplacian filter to determine image blur. The dataset should consist of high-quality images and should be stored in the /datasets directory.

### Labeling Images
Label the images using the labelImg software. For installation instructions, refer to the [labelImg repository](https://github.com/heartexlabs/labelImg). Define the classes in a text file named `predefined_classes.txt` located in `/labelImg/data`. Here are the predefined classes:
```
bot
duckie
stop_sign
road_sign
```
To label the images, open the dataset directory in the labelImg software.

### Dataset Split
Divide the labeled dataset into three sets: 85% for training, 7.5% for testing, and 7.5% for validation. The dataset split files `train.txt` and `valid.txt`, which include the path to each training and validation image, are included in this repository inside `/datasets`.

### YOLO Configuration Files
Prepare the YOLO configuration files. Create the `duckie.data` file and place it inside `/darknet/cfg`. Here is the content of the `duckie.data` file:
```
classes=4
train=datasets/train.txt
valid=datasets/valid.txt
names=data/duckie.names
backup=duckie_backup
```
Create the `duckie.names` file and place it inside `/darknet/data`. The file should contain the class names listed above.

Duplicate the `yolov3-tiny.cf`g file and name it `yolov3-tiny-duckie.cfg`. Make the following changes inside the `yolov3-tiny-duckie.cfg` file:
filters=27 (lines 127 and 171)
classes=4 (lines 135 and 177)

## Testing the Model
To test the model with the weights generated after training it with the provided dataset, run the [Colab notebook](https://colab.research.google.com/drive/1KTiGe3cxPZeqqvHbAlBw8Iej71HOL5aj?usp=sharing).
