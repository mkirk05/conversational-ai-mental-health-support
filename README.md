# Conversational AI for Mental Health Support

## Overview
This project implements a conversational AI system designed to provide supportive responses based on user emotional input. The system combines emotion classification, AI-generated responses and safety filtering to enable safe and context aware interaction.

---

## Features
- Emotion classification using TF-IDF and Logistic Regression
- AI-based response generation using OpenAI API
- Safety layer for detecting high-risk input
- Chat-based interface built with Streamlit

---
## Project Structure
```plaintext
app/               #Core logic (classification, response generation, safety)
data/              #Dataset used for training
models/            #Trained model and vectorizer
logs/              #Evaluation results
UI_app.py          #Main Streamlit interface
chat_app_2.py      #Conversational pipeline
```


---

## Setup Instructions

### 1. Clone the Repository
Clone or download this repository to your local machine.

---

### 2. Create a Virtual Environment
Create a virtual environment in the project directory:

```bash
python -m venv venv
```

Activate the environment:

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```
---

### 3. Install Dependencies
Install all required libraries using:

```bash
pip install -r requirements.txt
```
---

### 4. Set Up OpenAI API Key

This project requires an OpenAI API key for response generation.

1. Create an account at: https://platform.openai.com  
2. Generate an API key from your OpenAI dashboard  

Set the API key as an environment variable:

**Windows:**
```bash
setx OPENAI_API_KEY "your-api-key-here"
```

**Mac/Linux:**
```bash
export OPENAI_API_KEY="your-api-key-here"
```

Restart your terminal after setting the variable.

---

### 5. Run the Application

Start the Streamlit interface using:

```bash
streamlit run UI_app.py
```

The application will open in your browser, allowing interaction with the chatbot.

---
## Requirements
All required dependencies are listed in `requirements.txt`.

---

## Important Notice
This system is not a medical or diagnostic tool. It is intended for informational and supportive purposes only and should not be used as a substitute for professional mental health support.

---

## Repository
This repository contains the full implementation of the system described in the associated dissertation.
