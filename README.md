# Segmentation-Model-Serving
Repo for serving the segmentation model

### How to start the server?
- Cline the repository. (git clone <repo_name>)
- Create a folder called **Models** inside the flask folder and move the model inside that folder.
- Rename the model as **Unet.h5** 
- Open the command terminal, move to the folder where you have app.py(flask/app.py) and set the environment variable
    - command: export SM_FRAMEWORK=tf.keras (mac)
    - command: set SM_FRAMEWORK=tf.keras (windows)
- Then run the below command to start the flask server (localhost url: "http://localhost:5000/inference")
    - command: python3 -m flask --debug run
