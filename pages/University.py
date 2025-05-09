import streamlit as st

st.set_page_config(page_title="🎓 University", page_icon="🎓", layout="centered")

st.title("🎓 Bahçeşehir University")

# University Logo
st.image("bahcesehir_logo.png", width=400)  # Replace with your university logo file

# University Overview
st.markdown("""
**Bahçeşehir University (BAU)** is one of the leading private universities in Turkey, located in the heart of **Istanbul**.  
It is known for its strong emphasis on **international education**, **innovative research**, and **technological advancement**.

---  
**🌍 Location**: Beşiktaş, İstanbul, Turkey  
**🏫 Faculty**: Engineering and Natural Sciences  
**🏥 Department**: Bioengineering  
**📅 Founded**: 1998  
**💼 Motto**: *“Thinking Globally, Acting Locally.”*
""")

# Optional: Campus Image or Map
st.image("bau_campus.png", caption="Bahçeşehir University Campus - Beşiktaş", use_container_width=True)

# Optional: Highlight Links (uncomment and update if needed)
# st.markdown("[Visit Official Website](https://www.bau.edu.tr)")
# st.markdown("[Biomedical Engineering Department](https://bau.edu.tr/department-biomedical-engineering)")

# Optional Faculty Vision
st.markdown("""
---
### 🔬 Bioengineering at BAU

The Department of Bioengineering aims to train professionals who can combine engineering with medicine to develop novel healthcare technologies and improve patient care through interdisciplinary innovation.
""")
