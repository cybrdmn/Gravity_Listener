# Text Data: Web Scraping + Preprocessing (Lecture Materials)

This repository contains two hands-on notebooks for your lecture:
1. **Web Scraping (requests + BeautifulSoup)** — robust requests, CSS selectors, pagination, CSV export, ethics.
2. **Text Data Preprocessing** 

---

## 🚀 Quick Start

### Option A — Open directly in Google Colab (recommended)

> **Note:** Google Colab officially supports one‑click opening from **GitHub**, not GitLab.
> If you mirror your notebooks to GitHub, you can use these one‑click links:
>
> - Web Scraping:  
>   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1ZX-wvOOBkJf8q7WNXCofOEPxszWmWBmx)
>
> - Text Data Preprocessing:  
>   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1VIZHnLLOiIoVAz8FkHZJKIKY6mUFT46h)

### Option B — Stay on GitLab
Colab does not provide a native one‑click opener for GitLab. Use one of the approaches below:

1. **Clone in Colab at runtime**
   ```python
   !git clone https://gitlab.com/<namespace>/<project>.git
   %cd <project>
   ```
   Then open the desired `.ipynb` from the left file browser.

2. **Use GitLab Pages (raw file URL) + Colab upload**
   - Download the `.ipynb` and in Colab use **File → Upload notebook**.
   - Or host via **GitLab Pages** and share a regular download link.

References:
- Colab GitHub opener example: https://colab.research.google.com/github/ (official GitHub integration)
- Colab + GitLab via cloning/tokens: https://libinruan.gitlab.io/2020/02/07/How-to-Push-from-Colab-to-GitLab-A-Personal-Access-Token-Approach/

---

## 📚 Notebooks

- `Intro_AI_Web_Scraping.ipynb`  
  Covers: robust fetch with headers/timeouts, CSS selectors, pagination, robots.txt, polite delays, CSV, exercises, and a generated diagram.

- `Intro_AI_Text_preprocessing.ipynb`  
  Covers: Unicode normalization, fixing mojibake, URL removal, lowercasing, optional spaCy lemmatization, TF–IDF vectorization, quick baseline classifier, feature inspection.

---

## 🧰 Local Setup

```bash
# Create a fresh environment
python -m venv .venv && source .venv/bin/activate

pip install -r requirements.txt
# or individually:
pip install requests beautifulsoup4 pandas scikit-learn spacy ftfy unidecode matplotlib
python -m spacy download en_core_web_sm
```


