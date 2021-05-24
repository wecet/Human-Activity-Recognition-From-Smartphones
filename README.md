# Human-Activity-Recognition

## Pre-Requisites 

In order to run the Jupyter Notebooks you need quite a few Python packages. Running the below command in the CMD will automatically download the packages.

    pip install requirements.txt

## Data Collection

The data for this project was collected via AndroSensor. A free to use application on the Google Play Store. This app allows recording of the changes of the inertia sensors of your phone. For this project 4 sensors were chosen being:

    Gravity, Accelerometer, Linear Acceleration, Gyroscope
    
    
## Data Preprocessing

The initial data collected from the app was unsatisfactory and some processing had to be carried out. In order to match the data collected by the referenced paper from this study 'A Public Domain Dataset for Human Activity Recognition Using Smartphones' [Anguita et al.] some staticial operations had to be carried out, such as calculating the mean, entropy, sma and many more. But this was not easy, considering many duplicate or NaN values collected, so these had to be eliminated by a few lines of code.

## Data Analysis 

In order to assist in visualization of the clustering of both datasets, a t-SNE algorithm was run in order to help us visualize the data better and understand why some accuracies are not as good as expected.

![image](https://user-images.githubusercontent.com/73174341/119393130-d81e0e80-bcd0-11eb-98ea-932a0e0d85dc.png)


## Modelling
        
Finally, this project uses classification from 5 different supervised machine learning algorithms being:

    K Nearest Neigbours, SVM with RBF, SVM with Poly, Decision Trees and Logistic Regression.
    
The above was carried out twice, one with the mimicked data set containing * activities and the original dataset containing ** activities, although a Tennis dataset was also recorded but left out due to very poor classification.

    * Walking Upstairs, Walking Downstairs, Walking, Sitting, Laying and Standing
    ** Swimming, Cycling, Football, Jogging, Pushups and Jumprope
    
Upon running a Confusion Matrix is generated for each Supervised Learning Algorithm as shown below.

![image](https://user-images.githubusercontent.com/73174341/119392508-21ba2980-bcd0-11eb-9a15-96ed1a37aeb0.png)

#Resultantly, the highest classification accuracy recorded is 96%+ !
