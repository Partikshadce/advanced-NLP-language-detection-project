# app.py
import streamlit as st
from language_analyzer import LanguageAnalyzer
from visualizer import LanguageVisualizer

st.title("🌍 Advanced Language Detection & Analysis System")

text = st.text_area("Enter text to analyze:")

if st.button("Analyze"):
    if text.strip() == "":
        st.warning("Please enter some text!")
    else:
        # Analyze language
        analyzer = LanguageAnalyzer(text)
        language_name = analyzer.get_language_name()
        st.success(f"Detected Language: {language_name}")

        # Generate detailed report
        report = analyzer.generate_report()
        st.text_area("Detailed Report", report, height=300)

        # Visualizations
        visualizer = LanguageVisualizer()
        fig = visualizer.create_language_distribution_chart(analyzer)
        st.plotly_chart(fig, use_container_width=True)
