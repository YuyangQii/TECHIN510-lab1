
import streamlit as st

st.title("👋 Hi, my name is Yuyang Qi")

col1, col2 = st.columns(2)

with col1:
   st.subheader("👩‍🎨 About me")
   st.markdown("""
    - 🎓 Education:  
       University of  Wahington   
       Tsinghua University
    - 📚 Major:  
       Connected Devices 
       & Landscape Architecture      
    """)
   st.subheader("💡 Skills")
   st.markdown("""
    - UX Design
    - UX Research
    - Prototyping   
    """)
   st.subheader("🤩 Interests")
   st.markdown("""
    - Photography
    - Handicrafts
    - Painting  
    - xing'haoSleeping 😴           
    """)


with col2:
   image_path = 'images/photo.png'
   st.image(image_path, caption='at Mountain Rainier🗻')


st.markdown("I enjoy  painting, particularly watercolors. I also have a passion for photography and doing crafts, which enables me to explore and express my creativity from various perspectives.")

col1, col2 = st.columns(2)
with col1:
    image_path = 'images/photo2.png'
    st.image(image_path, caption='in Chongqing 🌆')

with col2:
    image_path = 'images/photo3.png'
    st.image(image_path, caption='LA 🌇')  

col1, col2 = st.columns(2)
with col1:
    image_path = 'images/panda.png'
    st.image(image_path, caption='Handmade Panda😍')

with col2:
    image_path = 'images/bunny.png'
    st.image(image_path, caption='Handmade Bunny🐇')  

image_path = 'images/painting.png'
st.image(image_path, caption='dramatis personae🎭')  

image_path = 'images/watercolor.png'
st.image(image_path, caption='classical gardens🏡')