# Protein Activity Visualizer 🧬

A Flask-based interactive web application that visualizes age-related changes in protein activity using a volcano plot and boxplot, and links them with scientific literature from PubMed.

## 🚀 Features
- 📊 Volcano plot: logFC vs adjusted p-value
- 🧬 Clickable genes → detailed view
- 📈 Boxplot (Young vs Old donors)
- 🔬 PubMed article titles (via NCBI E-utilities)

## ▶️ Run locally

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
Open in browser: http://127.0.0.1:5000