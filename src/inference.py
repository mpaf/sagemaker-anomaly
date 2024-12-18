import pickle
from io import BytesIO
import numpy as np
import os

def model_fn(model_dir):
    """Load the model for inference    
    Args:
        model_dir (str): The directory where model artifacts are stored
    Returns:
        model: The loaded model object
    """
    model_file = 'model.pkl'
    model_path = os.path.join(model_dir, model_file)
    
    # Load the model
    model = pickle.load(open(model_path, 'rb'))
    
    return model


def predict_fn(input_data, model):

    predictions = model.predict(input_data)
    
    # gives the distances to centroids
    dists = model.transform(input_data)[np.arange(len(predictions)), predictions]

    
    return np.vstack([predictions, dists])