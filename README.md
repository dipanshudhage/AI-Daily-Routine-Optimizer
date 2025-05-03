# 🧠 AI-Powered Daily Routine Optimizer

A smart and interactive Streamlit-based app that generates a personalized daily schedule based on your wake/sleep times, focus preferences, and activity goals.

---

## 🚀 Overview

This project helps users build an optimized daily routine with enhanced time management, tailored priorities, and smart scheduling. Designed especially for students, professionals, and anyone looking to improve productivity with balanced breaks, sleep, and personal growth time.

---

## 📌 Features

- ⏰ Wake-up and Sleep Time Setup  
- 🎯 Priority Selection (Study, Exercise, Relaxation, etc.)  
- 🧠 Peak Focus Hour Customization  
- 📅 Intelligent Hourly Task Distribution  
- 📊 Visual Time Distribution Pie Chart  
- 💡 Smart Suggestions for better productivity  
- 📥 Downloadable Schedule (.txt format)  
- 🖼️ Professional User Interface & Outcome Visualization  

---

## 🛠️ Tech Stack

- **Frontend & Logic**: [Streamlit](https://streamlit.io/)
- **Language**: Python 3.x
- **Libraries Used**:  
  - `pandas`  
  - `matplotlib`  
  - `datetime`  
  - `random`  
  - `streamlit`  

---

## 📂 Folder Structure

```
📁 ai-daily-routine-optimizer
│
├── 📁 app
│   ├── app.py
│   └── requirements.txt
│
├── 📁 assets
│   ├── interface.png
│   └── outcome.png
│
├── 📁 data
│   └── optimized_schedule.txt
│
├── 📁 doc
│   ├── presentation.pptx
│   └── report.pdf
│
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🔧 How to Run Locally

1. **Clone the repository:**

```bash
git clone https://github.com/dipanshudhage/AI-Daily-Routine-Optimizer.git
cd ai-daily-routine-optimizer/app
```

2. **Create a virtual environment (optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Run the app:**

```bash
streamlit run app.py
```

---

## 📈 Output Preview

| Interface | Outcome |
|-----------|---------|
| ![interface](../assets/interface.png) | ![outcome](../assets/outcome.png) |

---

## 📌 Future Enhancements

- Drag-and-drop custom time blocks  
- Save multiple routines for different weekdays  
- Add goal tracking and productivity analytics  
- Dark/light theme switching  
- Export to Google Calendar  

---

## 📜 License

This project is licensed under the [MIT License](./LICENSE).

---

## 🙌 Acknowledgments

- Streamlit community for an intuitive app framework  
- Open-source contributors and educators who inspired clean productivity tools
