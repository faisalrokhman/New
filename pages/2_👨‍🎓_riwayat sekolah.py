import streamlit as st

st.set_page_config(
    page_title="Riwayat Sekolah | faisal",
    page_icon="👨‍🎓",
    layout="wide"
)
st.title("BEBERAPA JENJANG PENDIDIKAN YANG SAYA LALUI SELAMA MASA HIDUP")

st.container()
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.subheader("MI Plus Nurul Huda")
   
with col2:
    st.subheader("MTs Plus AL Bukhori")
    
with col3:
    st.subheader("MA Plus AL Bukhori")
   
with col4:
    st.subheader("UNU Rombel AL Bukhori")

with st.container():
        col1, col2, col3, col4, = st.columns(4)
        with col1:
            st.caption("*Alamat : Jl. Cemara Kecipir - Losari - Brebes*")
        with col2:
            st.caption("*Alamat : Jl. Cemara Gg. At Taubah Rt. 06 Rw. 03, Sengon - Tanjung - Brebes*")
        with col3:
            st.caption("*Alamat : Jl. Cemara Gg. At Taubah Rt. 06 Rw. 03, Sengon - Tanjung - Brebes*")
        with col4:
            st.caption("*Alamat : Gedung BLKK Pesantren Al Bukhori, Jl. Cemara Gg. At Taubah Rt. 07 Rw. 03, Sengon - Tanjung - Brebes*")
   
   
st.container()
st.write("---")
col1, col2, col3, col4 = st.columns(4)
with col1:
   
    st.image("mi.png", width= 190)
with col2:
   
    st.image("mts.png", width= 190)
with col3:
    
    st.image("ma.png", width= 190)
with col4:
    
    st.image("unuu.png", width= 190)