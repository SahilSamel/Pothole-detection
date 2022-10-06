import os

test_images = [f for f in os.listdir('./data/obj/test/') if f.endswith('.jpg')]
import random
img_path = "./data/obj/test/" + random.choice(test_images);
print(img_path)

#test out our detector!
# ./build/Release/darknet.exe detect ./cfg/yolov4-custom.cfg ./backup/custom-yolov4-detector_best.weights {Insert img_path here} -dont-show imShow('.results/predictions.jpg')