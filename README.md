# Pothole-detection
Pothole Recognition using YOLO4

This model has been hosted using the roboflow API. It using a webcam to detect potholes in realtime.
Here's the link to the [model](https://pothole-detector-69.netlify.app/)

This is a deep learning model for detecting the potholes on roads. This model uses the YOLO-v4.

The total number of images in the dataset was 665 images. Of these images, 70 percent were for training, 20 percent for validation, and 10 percent for testing the effectiveness of the trained model. The images with their respective annotations are given in YOLO Darknet TXT format in the dataset folder, the application https://roboflow.ai was used to generate the dataset.

## Training

This model was trained using Google Colab. Dataset was directly downloaded through roboflow via the roboflow api. The .ipynb file can be used to train custom models too.The weights extracted from this training were then used to test and save the model locally.

The given custom cfg file for yolov4 was used in the training. This was configured for a Tesla T4 GPU.

## Local Training and Testing

Darkent needs to be configured before doing the following steps.

### Data segregation for training purposes-
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dataprocess.py - segregates the data ainto 2:- train and valid.

### Local Training -
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;train.py - Has training command line code given in it.

### Local Testing with trained weights-
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;test.py - Generates the path of a random image when executed. Given with it is the command line code that needs the image path to test the model on a random test image.

## Results

### mAP Calculation
The calculated mAP(0.5) = 90.02%

![image](https://user-images.githubusercontent.com/81075927/194372877-7e1db724-b04b-484b-abcd-4f8b881cc289.png)

### Testing the model
Testing with these weights, using the test.py on a randomly chosen test image.

![image](https://user-images.githubusercontent.com/81075927/194373327-d3005709-7985-47ee-ac3d-4f61c106c0e2.png)

Result of Testing

![image](https://user-images.githubusercontent.com/81075927/194373108-39301b64-2302-4d1e-82b9-589eedaa42ca.png)


