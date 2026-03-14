import streamlit as st
import pandas as pd
import joblib
from utils.geo_tracker import get_ip_from_url, track_location
from utils.feature_extraction import extract_url_features

# Load both trained ML models at startup
try:
    url_model = joblib.load('models/url_tree_model.pkl')
    text_model = joblib.load('models/text_nb_model.pkl')
    models_loaded = True
except FileNotFoundError:
    models_loaded = False

st.set_page_config(page_title="Phishing & Threat Analyzer", page_icon="🛡️", layout="wide")

st.title("🛡️ AI-Powered Phishing & Threat Analyzer")
st.markdown("Analyze websites, suspicious text, and track malicious infrastructure.")

if not models_loaded:
    st.error("⚠️ Models not found! Please run both `train_model.py` and `train_text_model.py`.")

# Create tabs
tab1, tab2, tab3 = st.tabs(["🔗 URL Analysis", "📄 Text Analysis", "🌍 Geo-Tracker"])

with tab1:
    st.subheader("Website & Domain Phishing Detection")
    url_input = st.text_input("Enter URL to analyze:", placeholder="https://example.com")
    
    if st.button("Analyze URL"):
        if url_input and models_loaded:
            with st.spinner("Extracting features and running ML models..."):
                features = extract_url_features(url_input)
                prediction = url_model.predict(features)[0]
                
                st.success("Analysis Complete!")
                if prediction == 1:
                    st.metric(label="Risk Assessment", value="High Risk", delta="🚨 Phishing Detected", delta_color="inverse")
                else:
                    st.metric(label="Risk Assessment", value="Low Risk", delta="✅ Potentially Safe")

with tab2:
    st.subheader("Email & Message Phishing Scanner")
    text_input = st.text_area("Paste suspicious email/message content here:")
    
    if st.button("Scan Text"):
        if text_input and models_loaded:
            with st.spinner("Analyzing text semantics..."):
                # Pass the raw text directly into the NLP pipeline
                prediction = text_model.predict([text_input])[0]
                
                st.success("Analysis Complete!")
                if prediction == 1:
                    st.metric(label="Threat Level", value="Critical", delta="🚨 Malicious Intent Detected", delta_color="inverse")
                    st.error("This text contains manipulative language, artificial urgency, or common phishing hooks.")
                else:
                    st.metric(label="Threat Level", value="Minimal", delta="✅ Safe / Normal Comm", delta_color="normal")
                    st.info("The language appears to be standard communication.")
        elif not text_input:
            st.warning("Please paste some text to analyze.")

with tab3:
    st.subheader("Mid-Strike Infrastructure Tracking")
    target_input = st.text_input("Enter Domain or IP Address:")
    if st.button("Track Target"):
        if target_input:
            with st.spinner("Tracing network routes..."):
                ip = get_ip_from_url(target_input) if not target_input.replace('.','').isdigit() else target_input
                if ip:
                    geo_data = track_location(ip)
                    if "Error" not in geo_data:
                        st.json(geo_data)
                        map_data = pd.DataFrame({'lat': [geo_data['Lat']], 'lon': [geo_data['Lon']]})
                        st.map(map_data)
                    else:
                        st.error("Could not retrieve geographical data.")
                else:
                    st.error("Could not resolve domain to IP.")