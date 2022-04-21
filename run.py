# This program prints Hello, world!
import requests, json
from datetime import date
import pandas as pd
import os 
imagesArray = ['gridlabd/master', 'openfido/cli']

def get_image_pull_count(image):
    response = requests.get(f"https://hub.docker.com/v2/repositories/{image}")
    data = response.json()
    return data['pull_count']

def recordDockerImagePullCount(images):

    # mm/dd/y
    today = date.today()
    d3 = today.strftime("%m/%d/%y")
    data = [d3]
    for image in images:
        count = get_image_pull_count(image)
        data.append(count)
    return data
data_array = recordDockerImagePullCount(imagesArray)
dirpath = os.getcwd()
output_path = os.path.join(dirpath,'output.csv')


df = pd.DataFrame([data_array])
# save to output csv file
df.to_csv(f'{output_path}', mode='a', index=False, header=False)
print(f"write file {output_path}")
