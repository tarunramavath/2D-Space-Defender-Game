#Project Name
CAR DIRTINESS AND DAMAGE DETECTION WITH SPECIFICATION

#Purpose
Car maintenance is really a hectic task when it comes to waiting for longer duration hence we can automate this task by recommending users based on their car condition

#Requirements
Tensorflow
Flask
PIL
matplotlib
requests
scipy
torch
pandas
#How to run this code
git clone https://github.com/Mak-3/Car-Dirtiness-and-Damage-detection
cd Car-Dirtiness-and-Damage-detection
python flask_app.py
open in localhost
output
Screenshot (14) Screenshot (24) Screenshot (28)

#Types of output
YOLOv5 will return image if damaged with bounding boxes namely of 4 possibilities

Scratch
Glass broken
Deformation
Broken
VGG16 will return output in String format in the cmd as either "messy" or "clean"
