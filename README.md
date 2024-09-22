# Dog-breed-classification-using-Deep-Learning-approach

## Project Overview
This project focuses on developing a deep learning-based MLOps system for object detection, specifically for identifying and classifying dog breeds. The project employs a YOLOv5 pre-trained model, which has been trained on a custom dataset of dog breed images. The system has been designed and implemented using both Python and Flask for backend processing, along with HTML for the user interface.

## Contents of the Repository
This repository contains the key components of the project, including the Jupyter Notebook used for model training and a folder containing the Flask web application code.

### 1. Jupyter Notebook (`Dog_Breed_Identification_with_YOLO.ipynb`)
The notebook documents the entire process of training the YOLOv5 object detection model using transfer learning on a custom dataset. It includes steps for data preprocessing, training, evaluation, and saving the trained model. The trained model is included in this repository- `mymodel.pt`
### 2. Flask Application (`/Myproject`)
This folder contains the code for the web application built using Flask. The application allows users to upload an image, and the model will predict and display the breed of the dog in the image.
The folder structure is as follows:

`app.py`: The main Flask application file that handles routing and prediction logic.
`templates/`: Contains HTML templates for the web pages.
`index.html`: The homepage where users can upload an image for classification.
`result.html`: The results page that displays the predicted dog breed after image processing.
`static/`: Contains static assets like CSS and JavaScript if needed.
`yolov5/`: This folder contains the YOLOv5 configuration files and related resources required for inference.

How to Run the Project
To run the project locally, follow these steps:

- Open the Myproject folder on vscode or other IDE
- Replace the directory of `mymodel.pt` in `app.py`
- Clone the YOLOv5 pre-trained model repository
```
!git clone https://github.com/ultralytics/yolov5.git```
```
```
cd yolov5
- pip install -r requirements.txt
- Replace the directory of yolov5.pt in app.py
```
- Run the `app.py` to launch the deployment server
```
python app.py
```
To clone this repository:
```
git clone [https://github.com/Bawamary/My-Final-Project.git](https://github.com/Ola-stathub/Dog-breed-classification-using-Deep-Learning-approach.git
