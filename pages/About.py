import streamlit as st

st.title("📘 About This Project")

st.markdown("""
### 🎯 Purpose of the Project

This project presents a machine learning-based system for predicting cardiovascular disease risk using non-invasive clinical inputs. Designed as a practical decision-support tool, it enables early detection and risk evaluation through a user-friendly interface, combining biomedical engineering principles with artificial intelligence.
""")

st.markdown("---")

st.subheader("👨‍💻 Developer")
col1, col2 = st.columns([1, 2])
with col1:
    st.image("ali_portrait_bw.png", width=150)
with col2:
    st.markdown("""
    **Name**: Ali Faiq Jari Alsaadawi   
    **Field**: Biomedical Engineering  
    **Role**: Developer & Researcher  
    **Focus**: AI-powered diagnostics, biomechanics, and digital health.
    """)

st.markdown("---")

st.subheader("👨‍🏫 Supervisor")
col3, col4 = st.columns([1, 2])
with col3:
    st.image("supervisor_portrait_bw.png", width=150)
with col4:
    st.markdown("""
    **Name**: Dr. Öğr. Üyesi Bora Büyüksaraç  
    **Position**: Thesis Supervisor  
    **Field**: Biomedical Engineering  
    **Institution**: Bahcesehir University  
    **Contact**: bora.buyuksarac@eng.bau.edu.tr  
    **Focus**: Medical Imaging, Image Processing, Magnetic Resonance
    Imaging (MRI), Perfusion Imaging, Cardiac Perfusion with MRI,
    Brain Perfusion with MRI, 3D Modeling

    """)

st.markdown("---")

st.markdown("""
📍 **University**: Bahcesehir University  
📅 **Thesis Year**: 2025  
📧 **Contact**: alifaiqjari@gmail.com  
💡 **Built With**: Python, Streamlit, Scikit-learn
""")
