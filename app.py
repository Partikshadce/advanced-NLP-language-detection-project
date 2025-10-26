import streamlit as st
from language_analyzer import LanguageAnalyzer
from visualizer import visualize_language_distribution
import os

st.set_page_config(page_title="Advanced NLP Language Detection", page_icon="🌍")

st.title("🌍 Advanced NLP Language Detection System")
st.write("This app detects the language of input text using advanced NLP models.")

# --- Text input section ---
text = st.text_area("✍ Enter text to analyze:", height=150)

if st.button("🔍 Detect Language"):
    if text.strip():
        try:
            analyzer = LanguageAnalyzer(text)
            lang_name = analyzer.get_language_name()
            st.success(f"✅ Detected Language: *{lang_name}*")
        except Exception as e:
            st.error(f"Error while detecting: {e}")
    else:
        st.warning("Please enter some text first!")

st.markdown("---")

# --- Optional batch processing section ---
st.subheader("📁 Batch Language Detection (optional)")
uploaded_file = st.file_uploader("Upload a .txt file containing multiple sentences:", type="txt")

if uploaded_file is not None:
    try:
        content = uploaded_file.read().decode("utf-8")
        st.write("File uploaded successfully!")

        # Create temporary file for batch processing
        temp_file = "temp_uploaded.txt"
        with open(temp_file, "w", encoding="utf-8") as f:
            f.write(content)

        # Use batch processor if available
        try:
            from batch_processor import process_folder
            result = process_folder(".")
            st.write("Detected languages for uploaded file:")
            st.write(result)
        except Exception:
            st.info("Batch processor not used; showing single detection instead.")
            analyzer = LanguageAnalyzer(content)
            st.success(f"Detected Language: *{analyzer.get_language_name()}*")

        # Cleanup temp file
        os.remove(temp_file)
    except Exception as e:
        st.error(f"Error: {e}")

st.markdown("---")
st.caption("Built with 💙 using Streamlit and the Advanced NLP Language Detection modules.")
