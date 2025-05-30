# 🌞 Solar Industry AI Assistant

An AI-powered tool that analyzes rooftop satellite imagery to assess solar panel installation potential, recommend configurations, and estimate return on investment (ROI). Built for homeowners, solar professionals, and industry interns.

---

## 🔍 Features

- 🛰️ *Vision AI*: Analyzes rooftops from satellite images and detects usable solar area.
- ⚡ *Installation Recommendation*: Suggests optimal number and type of solar panels.
- 💰 *ROI Calculator*: Computes cost, incentives, payback period, and savings.
- 📊 *User Interface*: Streamlit-based interface for image upload and analysis.

---


## 🚀 How to Run

### ▶️ Option A: Local (Recommended)

bash
# 1. Clone the repo or unzip the project folder
git clone  https://github.com/mastikhorr/solarAI.git

cd solar-ai-assistant

# 2. (Optional) Create virtual environment
python -m venv venv
venv\\Scripts\\activate  # On Windows
source venv/bin/activate # On Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app/main.py
