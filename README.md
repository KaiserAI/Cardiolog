# 🫀 Cardiolog: Explainable AI for Medical Decision Support
### A Neuro-Symbolic System combining Machine Learning and Logical Reasoning

![Python](https://img.shields.io/badge/Language-Python_3.x-3776AB?logo=python&logoColor=white)
![Logic](https://img.shields.io/badge/Reasoning-s(CASP)-blue)
![ML](https://img.shields.io/badge/AI-Scikit_Learn-F7931E?logo=scikit-learn)
![Focus](https://img.shields.io/badge/Focus-XAI_%2F_Healthcare-green)

> **Cardiolog** is a medical decision-support system designed to address the **lack of interpretability and accountability in clinical AI**.  
> Instead of returning opaque risk scores, the system provides **explicit, human-readable justifications** for each prediction using a **neuro-symbolic architecture**.

The project explores how statistical learning can be translated into **logical, inspectable reasoning pipelines**, making AI outputs more suitable for high-stakes and regulated environments.

---

## 🚀 Key Capabilities

* **🔍 Glass-Box Decision Support**  
  Translates opaque Random Forest decision paths into transparent logical rules that can be inspected, audited, and debated.

* **🗣️ Explainable Justifications**  
  Generates structured, natural-language explanations such as:  
  *“High risk BECAUSE cholesterol > 240 AND age > 50”*, enabling clinician-level understanding of model behavior.

* **🧠 Hybrid Intelligence Architecture**  
  Combines the predictive strengths of **Machine Learning** with the reasoning and traceability of **symbolic logic (Prolog / s(CASP))**.

* **🧬 Dynamic Patient Modeling**  
  New patient data is automatically converted into logical facts, enabling real-time inference and explanation without retraining the model.

---

## 🏗️ System Architecture

The system is organized as a three-layer pipeline that converts statistical patterns into logical proofs:

### 1. Learning Layer — Statistical Pattern Extraction
* Trains a **Random Forest Classifier** on the Cleveland Heart Disease dataset.
* Captures predictive structure while accepting limited interpretability at this stage.

### 2. Translation Layer — Model-to-Logic Compilation
* A custom **Tree-to-Logic compiler** (`translator.py`) traverses each decision tree and transpiles its paths into **s(CASP)-compatible predicates**.
* Each tree is treated as an independent reasoning agent, contributing partial evidence.

### 3. Reasoning Layer — Symbolic Inference
* Aggregates logical rules and patient-specific facts.
* Executes queries using **s(CASP)** to compute stable models.
* Produces a structured **justification tree**, rendered as HTML for inspection.

---

## 🛠️ Project Structure

```text
/
├── cardiolog/           # Core source code
│   ├── translator.py    # Decision Tree → Logic compiler
│   ├── main.py          # Pipeline orchestration and inference
│   └── ...
├── data/                # Clinical datasets (CSV)
├── prolog/              # Generated logical knowledge base
├── templates/           # HTML explanation templates
└── output/              # Reasoning traces and justification trees
