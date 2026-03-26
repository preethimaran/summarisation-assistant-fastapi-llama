# Summarisation Assistant

A fast, AI-powered application to summarise any text or content from a URL using **LLaMA 3.2** with **zero-shot learning**. Provides concise, accurate summaries with an interactive interface. Built using **FastAPI** and **Streamlit**



## Features

- Summarise plain text instantly  
- Summarise web page content via URL  
- Zero-shot summarisation using LLaMA 3.2  
- Streamlit-based frontend for easy interaction  

## Screenshots

![Link](https://github.com/user-attachments/assets/0f4159f4-863e-45c1-a7ab-4b2896eeb418)

---

![Text](https://github.com/user-attachments/assets/1c16ae66-ddbd-4db9-b02a-d76a0eefb664)

## Quick Start

1. **Clone the repo:**

```bash
git clone <repository-URL>
cd <repository_name>
```

2. **Install Dependencies**

```bash
pip install -r requirements.txt
```
3. **Run the Backend API**

```bash
uvicorn main:app --reload
```

3. **Run Frontend**

```bash
streamlit run frontend/app.py
```


## Project Structure

```text

Summarisation_assistant/
├─ README.md                     # Project description and instructions
├─ requirements.txt              # Python dependencies
├─ .gitignore                    # Git ignore rules
├─ main.py                       # FastAPI backend entry point
│
├─ app/
│  ├─ __init__.py
│  ├─ config.py                  # Config variables (API tokens and model names)
│  │
│  ├─ models/
│  │  ├─ __init__.py
│  │  └─ summariser.py           # LLaMA 3.2 model wrapper
│  │
│  ├─ routes/
│  │  ├─ __init__.py
│  │  └─ summarise.py            # API endpoints for text/URL summarisation
│  │
│  └─ utils/
│     ├─ __init__.py
│     └─ fetch.py                # Functions to fetch and parse text from URLs
│
└─ frontend/
   ├─ __init__.py
   └─ app.py                     # Streamlit frontend interface

```

## Author
Preethi Maran