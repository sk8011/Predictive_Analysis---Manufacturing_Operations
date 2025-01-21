# Predictive_Analysis---Manufacturing_Operations

API documentation for this project can be found at: 
https://planetary-comet-997012.postman.co/workspace/New-Team-Workspace~3bc2f509-1b9e-44cc-8bc4-8c831cbdf355/collection/37602694-eb6ffe23-1b9b-4845-a4fb-cbc1341f74ee?action=share&creator=37602694

Pre-requisites:
Inside the working directory where "api.py" is located, make sure you create 2 folders named, "model" and "uploaded_files" for storing the trained model and the training data respectively.
Also, check "api.py" file and make sure all dependencies are met and all libraries are installed in the environment before running the api server.

To run the api server locally, download the "API" folder and then inside the directory, open command prompt. </br>
In command prompt, type: "uvicorn api:app --host 127.0.0.1 --port 8000 --reload". This will host and run the api server at http://localhost:8000.
(make sure you install uvicorn using "pip install uvicorn[standard]" in the environment beforehand)

Now, simply follow the API documentation whose source I've provided above to make requests and get predictions.

Note: Training data i.e. "train.csv" can be found inside the "ML_model" folder and inside that folder, I've also provided the jupyter notebook where I've done all the data preprocessing, analysis and process of selecting right estimator.
