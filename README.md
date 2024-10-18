# PlasticCheckup
Plastic Classification App

## Project Description

<p align="justify">The Plastic Classification App is a machine learning application that uses a trained convolutional neural network (CNN) to classify different types of plastic based on images. It can help identify plastic types such as HDPE, LDPE, PET, PP, PS, PVC, and others.<br>
So we will be collecting plastic waste from government or NGO's, segregate it and then sell it to the companies recycling plastic waste as per thier need. Like - IOC(Indian Oil Corporation) utilises PET plastic to make uniforms for its employees.</p>

## Features

- Upload and classify plastic images.
- Real-time prediction using a trained CNN model.
- User-friendly Streamlit frontend.

## Technologies Used
- Python
- TensorFlow and Keras
- Streamlit
- PIL (Python Imaging Library)

## Traditional work

<p align="justify">Traditionally, the segregation of plastic waste has been performed by manually inspecting the symbols on the back of plastic materials. These symbols, standardized by the resin identification code system, indicate the type of plastic used in the product. The codes range from 1 to 7 which is known as Resin Identification Code, each representing a different category of plastic which is shown by the figure given below </p>
![image](https://github.com/user-attachments/assets/93e80e79-8ce8-40ad-9397-94ad2eb0d5fe)

## Pseudo Code
•	Import necessary libraries: os, numpy, ImageDataGenerator, ResNet50, Dense, GlobalAveragePooling2D, Model
•	Define paths to labeled image data: train_data_dir, val_data_dir
•	Create data augmentation and normalization:
    -train_datagen with rescaling, rotation, width shift, height shift, and horizontal flip
    -val_datagen with only rescaling
•	Load pre-trained ResNet50 model without the top layers
•	 Add custom classification head to the model:
    -GlobalAveragePooling2D layer
    -Dense layer with 1024 units
    -Dense layer with 7 units and 'softmax' activation
•	Create the final model
•	Compile the model with 'categorical_crossentropy' loss and 'accuracy' as a metric
•	Train the model with training data for 10 epochs and validation data
•	Save the trained model to the specified path and print confirmation message

## Architecture
![WhatsApp Image 2024-05-19 at 21 48 11_5dfa546d](https://github.com/user-attachments/assets/1a459186-d574-410c-be80-6c359a0c7d00)
![WhatsApp Image 2024-05-19 at 21 53 38_7caf5c9a](https://github.com/user-attachments/assets/055823e8-1269-4c85-bf88-f338bb8452a4)

## Results
Landing Page
![image](https://github.com/user-attachments/assets/c5d94f1d-1191-4a2c-be3b-dcfee1de3d48)

Admin Dashboard
![image](https://github.com/user-attachments/assets/eb135ad2-dce4-4761-ae6f-c93461e09a26)
![image](https://github.com/user-attachments/assets/65c14132-0bd5-407e-8f28-52d14563cc65)


