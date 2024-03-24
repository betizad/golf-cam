import streamlit as st
from streamlit_image_select import image_select

st.set_page_config(layout="wide", page_title="Otelfingen Webcams")
st.markdown("### Otelfingen Webcams")

img = image_select(
    label="Select a webcam",
    images=[
        "https://www.golfparks.ch/Frontend/Sublayouts/Modules/ApplicationModules/Weather/Data/Web-Cams/Otelfingen/image-OF00001.jpg",
        "https://www.golfparks.ch/Frontend/Sublayouts/Modules/ApplicationModules/Weather/Data/Web-Cams/Otelfingen/image-OF00002.jpg",
        "https://www.golfparks.ch/Frontend/Sublayouts/Modules/ApplicationModules/Weather/Data/Web-Cams/Otelfingen/image-OF00003.jpg",
        "https://www.golfparks.ch/Frontend/Sublayouts/Modules/ApplicationModules/Weather/Data/Web-Cams/Otelfingen/image-OF00004.jpg",
        "https://www.golfparks.ch/Frontend/Sublayouts/Modules/ApplicationModules/Weather/Data/Web-Cams/Otelfingen/image-OF00005.jpg",
    ],
    captions=["Cam Range Mats", "Cam2", "Cam3", "Cam Putting", "Cam5"],
    use_container_width=False,
    
)
# print(img)
st.image(img)
