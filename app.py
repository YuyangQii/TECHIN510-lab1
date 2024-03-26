
import streamlit as st

st.title("👋Hi, my name is yuyang")

col1, col2 = st.columns(2)

with col1:
   st.subheader("👩‍🎨About me")
   st.markdown("""
    - School:  University of Wahington  &  Tsinghua University
    - Major:  Connected Devices  &  Landscape Architecture      
    """)
   st.subheader("💡Skills")
   st.markdown("""
    - UX Design
    - UX Research   
    """)

with col2:
   image_path = 'images/photo.png'
   st.image(image_path, caption='Mountain Rainier')


st.subheader("I enjoy  painting, particularly watercolors. I also have a passion for photography and doing crafts, which enables me to explore and express my creativity from various perspectives.")