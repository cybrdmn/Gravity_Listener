# 📘 Introduction to Data Analysis with Python – Course Materials

Welcome!  
This repository contains interactive notebooks for the **Introduction to Data Analysis with Python** course.  
You can run them directly in **Google Colab** or locally using **Jupyter Notebook**.

_Last updated: 2025-11-03_

---

## 🧠 Part 1 — Working with Google Colab

**What is Google Colab?**  
Google Colab (*Collaboratory*) is a free, cloud-based environment that lets you write and execute Python code inside your browser—no installation required.  
It provides:
- Pre-installed Python packages (NumPy, Pandas, Matplotlib, Seaborn, etc.)
- Free CPU and limited GPU runtime
- Integration with Google Drive for saving notebooks

### ✅ How to Use It
1. Open a notebook link (`.ipynb`) → click **“Open in Colab.”**  
2. Select **“Connect”** in the top-right corner to start the runtime.  
3. Run code cells with **Shift + Enter** or the ▶️ button.  
4. Use **+ Code** / **+ Text** to add your own cells.  
5. Save your work via **File → Save a copy in Drive** (recommended).  

> **Tip:** If you upload data files, use the folder icon (📁) → “Upload to session storage” or mount your Google Drive.  
> Session files are temporary, so keep copies in Drive if you need them later.

### 🔍 Common Colab Functions
| Function | Description |
|-----------|--------------|
| `!pip install package_name` | Install additional Python libraries |
| `from google.colab import drive; drive.mount('/content/drive')` | Connect your Google Drive |
| `!ls` | List files in the current directory |
| `%time` / `%timeit` | Measure execution time |

---

## 💻 Part 2 — Working with Jupyter Notebook (Local Setup)

**What is Jupyter Notebook?**  
Jupyter Notebook is an open-source, interactive environment where you can combine **Python code**, **text explanations**, **formulas**, and **visualizations** in a single document.

### 🛠️ Installation Options

**Option 1 – Anaconda (Recommended):**
- Download from [https://www.anaconda.com](https://www.anaconda.com)
- Open **Anaconda Navigator → Jupyter Notebook**

**Option 2 – pip Installation (Advanced):**
```bash
pip install notebook
jupyter notebook
```

### 🚀 How to Run a Notebook
1. Launch Jupyter Notebook → a browser tab will open.  
2. Navigate to the folder containing `.ipynb` files.  
3. Click a file to open it.  
4. Run cells with **Shift + Enter**.

### 🧭 Main Features
- Markdown cells for explanations and instructions  
- Code cells for Python execution  
- Integrated charts (Matplotlib, Seaborn, Plotly, etc.)  
- Autosaving and export to HTML / PDF  

> **Tip:** Use short, meaningful cell titles and one concept per cell — it keeps notebooks clear and readable.

---

## 📂 Repository Structure

```
├── 01_Intro_Data_Analysis_Python_Jupyter.ipynb
├── 02_Data_Wrangling_and_Visualization.ipynb
└── README.md
```

---

## 🔗 Open Notebooks in Google Colab

You can open the notebooks directly by clicking the buttons below:  

| Notebook | Open in Colab |
|-----------|----------------|
| **01 – Introduction to Data Analysis with Python & Jupyter** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](YOUR_NOTEBOOK_1_URL) |
| **02 – Data Wrangling and First Visualizations** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](YOUR_NOTEBOOK_2_URL) |

> Replace `YOUR_NOTEBOOK_1_URL` and `YOUR_NOTEBOOK_2_URL` with the actual links to the notebooks once uploaded to GitLab or Google Drive.

---

## 🧩 Suggested Learning Order
1. **Notebook 1 – Introduction to Data Analysis with Python & Jupyter**  
   - Basics of Python, NumPy, Pandas, and simple visualization  
2. **Notebook 2 – Data Wrangling and First Visualizations**  
   - Handling missing values, grouping, sorting, and bar plots  

---

## 💬 Need Help?

If you get an error in Colab or Jupyter:
- Check that the runtime is **Python 3**
- Restart the kernel (**Runtime → Restart runtime**)  
- Re-run all cells from the top  

For course questions, please contact your instructor or post in the discussion forum.
