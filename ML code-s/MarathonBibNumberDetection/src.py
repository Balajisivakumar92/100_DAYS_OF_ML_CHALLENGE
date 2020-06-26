import os 
from google.cloud import vision 
import pandas as pd 
import io
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"Balajivideo-094a4b7f77e2.json"

client = vision.ImageAnnotatorClient()

image_path = "img1.jpg"

with io.open(image_path, 'rb') as image_file:
    content = image_file.read()

# construct image instance 
image = vision.types.Image(content=content)

# annotate Image Response
response = client.text_detection(image=image)  # returns TextAnnotation
# df = pd.DataFrame(columns=['locale', 'description'])

texts = response.text_annotations

for text in texts:
    print(text.description)
    vertices = (["{}:{}".format(vertex.x, vertex.y)
                  for vertex in text.bounding_poly.vertices])
    print("annotations",vertices)
