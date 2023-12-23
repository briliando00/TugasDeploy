import streamlit as st
import google.generativeai as palm
from dotenv import load_dotenv
import os

# Konfigurasi Streamlit
st.set_page_config(page_title="Chat with Chef App", page_icon="🍳", layout="centered")

# Load environment variables
load_dotenv()

API_KEY = os.environ.get("AIzaSyB0a6ECvYgvgCGAUluyvyeNDuuK2C4_6Zc")
palm.configure(api_key=API_KEY)

def main():
    # Header dengan animasi dan efek visual
    st.image("./1.gif", use_column_width=True)
    st.title("Chat with Chef 🍲")
    
    st.write("Enter your ingredients below and let's cook up some text!")
    
    # Input dari pengguna dengan fitur hover
    prompt = st.text_area("Your Ingredients:", placeholder="Enter your ingredients here...", height=100, help="Enter ingredients for the recipe.")
    
    # Tombol dengan animasi saat ditekan
    if st.button("Cook!", help="Let's generate some text!"):
        with st.spinner("Cooking up some text..."):
            model = "models/text-bison-001"
            response = palm.generate_text(model=model, prompt=prompt, max_output_tokens=1024)
            
            # Menampilkan respons dengan efek suara
            st.audio("./cooking_sound.mp3", format="audio/mp3")
            st.subheader("Chef's Recipe 📜")
            st.markdown(response.result, unsafe_allow_html=False)

if __name__ == "__main__":
    main()
