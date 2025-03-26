# HMD-GUI
Hybrid Malware Detection GUI Application

### 🛡️ Hybrid Malware Detector  
**A powerful AI-driven hybrid malware detection system utilizing Static & Dynamic Analysis with Machine Learning.**  

![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![PyTorch](https://img.shields.io/badge/PyTorch-%F0%9F%94%A5-red) ![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 Overview  
The **Hybrid Malware Detector (HMD)** is an advanced malware classification system that combines **Static Analysis (RF & SVM)** with **Dynamic Analysis (CNN-based Image Classification)**. It efficiently detects and categorizes malware using a hybrid approach, making it both fast and accurate.  

---

## ⚙️ Features  
✅ **Hybrid Approach**: Combines machine learning for static analysis and deep learning for dynamic analysis.  
✅ **Static Analysis**: Extracts PE file features using **LIEF** and classifies malware using **Random Forest (RF) & Support Vector Machine (SVM)**.  
✅ **Dynamic Analysis**: Converts execution traces into images and classifies them using a **CNN-based image classifier**.  
✅ **Real-Time Detection**: Optimized for speed and accuracy.  
✅ **Standalone GUI**: Built using **PyQt6** for easy interaction.  

---

## 🏗️ Project Structure  
```bash
HybridMalwareDetector/
│── data/                  # Dataset directory (Benign & Malware samples)
│── ml_models/             # Trained model files (SVM, RF, CNN)
│── feature_extraction/    # Static & Dynamic feature extractors
│── gui.py                 # PyQt6 GUI implementation
│── requirements.txt       # Dependencies
```

---

## 🚀 Installation  

### 🔹 Prerequisites  
- Python 3.10+  
- **Install dependencies**:  
```bash
pip install -r requirements.txt
```

---

## 🔥 Usage  
### 1️⃣ **Run the Malware Detector GUI**  
```bash
python gui.py
```

### 2️⃣ **Detect Malware**  
- Upload a PE file for static analysis and CNN-based dynamic analysis.  
- View classification results & malware probability.  

