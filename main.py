import streamlit as st
from streamlit_image_select import image_select

st.set_page_config(layout="wide", page_title="Golf Webcams")

images=[]
captions=[]

location = st.sidebar.selectbox(
                              'Choose Location:',
                              ('Otelfingen', 'Holzhäusern', 'Winterberg')
                            )
page_title=f"{location} Webcams"

if location=="Otelfingen":
    images=[
        "https://www.golfparks.ch/Frontend/Sublayouts/Modules/ApplicationModules/Weather/Data/Web-Cams/Otelfingen/image-OF00001.jpg",
        "https://www.golfparks.ch/Frontend/Sublayouts/Modules/ApplicationModules/Weather/Data/Web-Cams/Otelfingen/image-OF00002.jpg",
        "https://www.golfparks.ch/Frontend/Sublayouts/Modules/ApplicationModules/Weather/Data/Web-Cams/Otelfingen/image-OF00003.jpg",
        "https://www.golfparks.ch/Frontend/Sublayouts/Modules/ApplicationModules/Weather/Data/Web-Cams/Otelfingen/image-OF00004.jpg",
        "https://www.golfparks.ch/Frontend/Sublayouts/Modules/ApplicationModules/Weather/Data/Web-Cams/Otelfingen/image-OF00005.jpg",
    ]
    captions=["Cam Range Mats", "Cam2", "Cam3", "Cam Putting", "Cam5"]
elif location=="Holzhäusern":
    images=[
        "https://www.golfparks.ch/Frontend/Sublayouts/Modules/ApplicationModules/Weather/Data/Web-Cams/Holzhaeusern/image01.jpg",
        "https://www.golfparks.ch/Frontend/Sublayouts/Modules/ApplicationModules/Weather/Data/Web-Cams/Holzhaeusern/image02.jpg"
    ]
    captions=["Range", "Putting"]
elif location=="Winterberg":
    images = ["https://cam.golf-winterberg.ch:65443/record/current.jpg"]
    captions = ["Cam"]
else:
    pass
    
st.markdown(f"### {page_title}")
img = image_select(
    label="Select a webcam",
    images=images,
    captions=captions,
    use_container_width=False
)
st.image(img)
