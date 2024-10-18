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

## Pseudo Code
•	Import necessary libraries: os, numpy, ImageDataGenerator, ResNet50, Dense, GlobalAveragePooling2D, Model<br>
•	Define paths to labeled image data: train_data_dir, val_data_dir<br>
•	Create data augmentation and normalization:<br>
    -train_datagen with rescaling, rotation, width shift, height shift, and horizontal flip<br>
    -val_datagen with only rescaling<br>
•	Load pre-trained ResNet50 model without the top layers<br>
•	 Add custom classification head to the model:<br>
    -GlobalAveragePooling2D layer<br>
    -Dense layer with 1024 units<br>
    -Dense layer with 7 units and 'softmax' activation<br>
•	Create the final model<br>
•	Compile the model with 'categorical_crossentropy' loss and 'accuracy' as a metric<br>
•	Train the model with training data for 10 epochs and validation data<br>
•	Save the trained model to the specified path and print confirmation message<br>

## Architecture
![WhatsApp Image 2024-05-19 at 21 48 11_5dfa546d](https://github.com/user-attachments/assets/1a459186-d574-410c-be80-6c359a0c7d00)
![WhatsApp Image 2024-05-19 at 21 53 38_7caf5c9a](https://github.com/user-attachments/assets/055823e8-1269-4c85-bf88-f338bb8452a4)

## Results
### Landing Page
![image](https://github.com/user-attachments/assets/c5d94f1d-1191-4a2c-be3b-dcfee1de3d48)

### Admin Dashboard
![image](https://github.com/user-attachments/assets/eb135ad2-dce4-4761-ae6f-c93461e09a26)
![image](https://github.com/user-attachments/assets/65c14132-0bd5-407e-8f28-52d14563cc65)


