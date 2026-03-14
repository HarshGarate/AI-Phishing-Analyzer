# 🛡️ AI-Powered Phishing & Threat Analyzer

This repository contains an end-to-end, machine learning-based cybersecurity application designed to detect phishing attempts and analyze mid-strike threat infrastructure. It provides real-time risk assessments for URLs, scans communication text for manipulative intent, and maps the hosting infrastructure of suspicious domains.

## 🚀 Project Features

1. **Website & Domain Phishing Detection:**
   - Extracts mathematical features from raw URLs (length, IP obfuscation, sub-domain chaining).
   - Utilizes a trained Decision Tree Classifier to assess the probability of a URL being malicious.
2. **Email & Message Phishing Scanner:**
   - Leverages Natural Language Processing (NLP) using TF-IDF vectorization.
   - Applies a Naive Bayes classification model to detect social engineering and artificial urgency in text.
3. **Mid-Strike Infrastructure Tracking:**
   - Resolves domains to their underlying IP addresses.
   - Uses an external API to geolocate the hosting infrastructure, identifying the ISP, country, and city to aid in firewall rule creation and threat intelligence gathering.

## 🛠️ Technology Stack

- **Frontend / UI:** Streamlit
- **Machine Learning:** Scikit-Learn, Pandas
- **Data Processing:** Regular Expressions (Regex), NLP (TF-IDF)
- **Deployment:** AWS EC2 (Ubuntu)

## ⚙️ Local Installation & Usage

1. **Clone the repository:**
   ```bashhttps://github.com/HarshGarate/AI-Phishing-Analyzer.git]
   cd ai-phishing-analyzer