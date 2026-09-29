# AI Internship Projects — DecodeLabs

Foundational AI projects built during my AI Automation Internship at **DecodeLabs** (Batch 2026). Each project focuses on core AI/ML concepts, implemented from scratch in Python.

---

## Project 1: Rule-Based AI Chatbot

A simple chatbot that responds to predefined user inputs using dictionary-based logic — no machine learning involved. Demonstrates control flow, input sanitization, and decision-making fundamentals.

**Key Features:**
- Handles greetings, questions, and exit commands
- Case-insensitive input matching
- Dictionary lookup with fallback response for unknown inputs
- Runs in a continuous loop until the user exits

**Tech Used:** Python

**How to Run:**
```bash
python chatbot.py
```

---

## Project 2: Data Classification Using AI

A supervised machine learning model that classifies Iris flowers into 3 species (Setosa, Versicolor, Virginica) using the K-Nearest Neighbors (KNN) algorithm.

**Key Features:**
- Loads and explores the Iris dataset
- Splits data into training (80%) and testing (20%) sets
- Scales features using StandardScaler
- Trains a KNN classifier and evaluates performance using Accuracy, Confusion Matrix, and F1 Score

**Tech Used:** Python, scikit-learn

**How to Run:**
```bash
pip install scikit-learn numpy
python classification.py
```

---

## Project 3: AI Recommendation Logic — Tech Stack Recommender

A content-based recommendation engine that suggests the best-matching career paths based on a user's skills. Uses TF-IDF vectorization and Cosine Similarity to measure how closely a user's skill set aligns with different job roles.

**Key Features:**
- Takes user input (minimum 3 skills)
- Converts skills and job requirements into numerical vectors (TF-IDF)
- Calculates similarity scores using Cosine Similarity
- Returns the Top 3 most relevant career paths with match percentage

**Tech Used:** Python, pandas, scikit-learn

**Files:**
- `tech_stack_recommender.py` — main script
- `raw_skills.csv` — dataset of job roles and required skills

**How to Run:**
```bash
pip install pandas scikit-learn
python tech_stack_recommender.py
```

---

## About Me

**Rubayat** — AI Automation Freelancer, specializing in n8n workflows, chatbot development, and digital automation solutions.


- 📧 Contact: rubayat.ch50@gmail.com
