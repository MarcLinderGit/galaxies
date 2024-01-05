# Load libraries
import requests
import io
import numpy as np
import os

# Loads data from url
def make_request(url):
    print("Requesting data from {}...".format(url))
    response = requests.get('https://content.codecademy.com/courses/deeplearning-with-tensorflow/'+url)
    response.raise_for_status()
    response_data = io.BytesIO(response.content)
    return response_data

# Loads galaxy data
def load_galaxy_data():
  
  # If cached file not found, loads data from url
  if not os.path.isfile('data\cached_data.npz'):
     response_data = make_request(url='galaxydata.npz')

     with open("data\cached_data.npz","wb") as save_file:
      save_file.write(response_data.read())
 
  # Load data using NumPy
  data = np.load('data\cached_data.npz')

  print("Successfully loaded galaxy data!")
  
  return data["data"],data["labels"]