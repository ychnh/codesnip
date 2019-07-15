# Commands
* ./darknet detector train cfg/caltech.data cfg/yolov3-tiny.cfg weights/yolov3-tiny.weights -clear 1
* Command for outputting at lower threshold for results


# Custom cfg comparision
* custom removed anchors 1603/8.7 = 184.2 on 1 card
* default 1603/10.2 = 157.1 on 1 card

But the performance of default much better. (Maybe it was trained for longer?)
It was alot worse.

* custom kept anchors 

# Links
* [yolo output in details](https://timebutt.github.io/static/understanding-yolov2-training-output/)
* [yolo output specifics](https://github.com/AlexeyAB/darknet/issues/636)
* [yolo learning rate](https://github.com/pjreddie/darknet/issues/701)
* [yolo training your own](https://github.com/AlexeyAB/darknet#how-to-train-to-detect-your-custom-objects)


# Key points
* The input size is really important. Because it really helps to detect.


# Project Flow
* First week 

* Intial read of literature

* Try different methods
  * Hog (Haar) method
  * Cascade method
  
* Research on image processing and different networks
  * Reading papers of RCNN, Fast RCNN, Faster RCNN
* Inspected various datasets
   * INRIA, CityScapes, Caltech Ped, Kaist Ped
* Subjected preliminary tests and model evaluation
  * Differences between INRIA and Caltech Ped

* Alot of hang time on setting up/ getting comfortable with remote desktop workflows

* Research on Yolo
  * Comparing different
