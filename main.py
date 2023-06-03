import openai
from PIL import Image
import streamlit as st
from apikey import apikey

def generate_image(image_description):
  img_response = openai.Image.create(
    prompt = image_description,
    n=1,
    size="512x512")
  img_url = img_response['data'][0]['url']
  return img_url

st.set_page_config(page_title="DALL.E 2 Image Generation")

openai.api_key = apikey

st.title('DALL.E 2 Image Generation')
st.subheader("Powered by OpenAI and Streamlit")
img_description = st.text_input('Image Desription')

if st.button('Generate Image'):
    generated_img = generate_image(img_description)
    st.image(generated_img)
