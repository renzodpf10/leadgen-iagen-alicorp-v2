
from transformers import pipeline

def load_image_generator():
    return pipeline("text-to-image", model="stabilityai/stable-diffusion-2", scheduler="DDIMScheduler")
