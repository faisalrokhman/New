import streamlit as st

st.set_page_config(
    page_title="Organizational Experience|Nailiyah",
    page_icon="👨‍🎓",
    layout="wide"
)

st.title("Pengalaman Organisasi")
st.write("Hanya Satu Organisasi Yang Saya Ikuti; ")

st.container()
col1, = st.columns(1)
with col1:
    st.subheader("Team Readaksi Plural")
   

st.container()
st.write("---")
col1, = st.columns(1)
with col1:
   
    st.image("plural.png", width= 190)

st.container()
st.write("---")
col1, = st.columns(1)
with col1:
    st.write("*Menjabat Sebagai Wakil Pimpinan Team Redaksi Plural*")
   