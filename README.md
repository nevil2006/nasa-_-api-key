# 🚀 NASA Space Dashboard 🌌

A visually interactive space dashboard using NASA public APIs. Built with **Streamlit**, **Plotly**, and **Python**, it showcases:

- 🌠 Astronomy Picture of the Day (APOD)
- 🪐 Asteroids Near Earth
- 🛰️ ISS Tracker
- 🔴 Mars Rover Photos
- 🌤️ Space Weather (Coming Soon)
- 🧠 NASA Patents Explorer (Planned)

## 📦 Features

- Clean, tabbed Streamlit interface
- Real-time data fetched from NASA APIs
- Visualizations using Plotly
- Modular and extensible layout

## 🚀 Output Preview

Here is how the NASA Space Dashboard looks:

![Dashboard Preview](ouput.png)

## 🚀 Getting Started

1. Clone the repository:

```bash
git clone https://github.com/yourusername/nasa-dashboard.git
cd nasa-dashboard

Create a virtual environment (optional but recommended):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
Install dependencies:

2.
```bash
pip install -r requirements.txt

3. Run the app:
```bash
streamlit run space.py

🔑 API Key Setup
Get your NASA API key from api.nasa.gov, then set it in the code like this:


API_KEY = "YOUR_KEY_HERE"

Or use environment variables for better security.

📁 Project Structure
markdown

nasa-dashboard/
├── space.py
├── requirements.txt
├── README.md
└── assets/
    └── demo.png
🛠️ Built With
Streamlit

NASA APIs

