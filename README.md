# 🫀 Cardiolog: Explainable AI for Medical Diagnosis
### Neuro-Symbolic System combining Machine Learning & Logical Reasoning

![Python](https://img.shields.io/badge/Language-Python_3.x-3776AB?logo=python&logoColor=white)
![Logic](https://img.shields.io/badge/Reasoning-s(CASP)-blue)
![ML](https://img.shields.io/badge/AI-Scikit_Learn-F7931E?logo=scikit-learn)
![Focus](https://img.shields.io/badge/Focus-XAI_%2F_HealthTech-green)

> **Cardiolog** is a diagnostic support system that addresses the "Black Box" problem in medical AI. Unlike standard predictive models that output a probability without context, Cardiolog uses a **Neuro-Symbolic architecture** to provide transparent, human-readable justifications for every diagnosis using **Answer Set Programming (ASP)**.

---

## 🚀 Key Features

* **🔍 Glass-Box Diagnosis:** Converts opaque Random Forest decision trees into transparent logical rules.
* **🗣️ Natural Language Explanations:** Generates human-readable justifications for why a specific risk level was predicted (e.g., *"Patient has high risk BECAUSE cholesterol > 240 AND age > 50"*).
* **🧠 Hybrid Intelligence:** Combines the predictive power of **Machine Learning** (Random Forest) with the reasoning capabilities of **Prolog/s(CASP)**.
* **🧬 Dynamic Patient Modeling:** Allows the ingestion of new patient data, converting clinical variables into logical facts for real-time inference.

---

## 🏗️ System Architecture

The system operates on a three-layer architecture designed to translate statistical patterns into logical proofs:

1.  **Learning Layer (Python/Scikit-learn):**
    * Trains a **Random Forest Classifier** on the Cleveland Heart Disease dataset.
    * Extracts decision paths from the ensemble of trees.

2.  **Translation Layer (Custom Algorithm):**
    * **Tree-to-Logic Compiler:** A specialized algorithm (`translator.py`) iterates through the decision trees and transpiles them into **s(CASP)** compatible predicates.
    * Each tree in the forest acts as an independent "doctor" offering a logical opinion.

3.  **Reasoning Layer (s(CASP)):**
    * Aggregates the logical rules and patient data (facts).
    * Executes a query to find the **Answer Set** (the most stable model).
    * Outputs a justification tree rendered as HTML for the end-user.

---

## 🛠️ Project Structure

```text
/
├── cardiolog/           # Source code package
│   ├── translator.py    # Core logic: Compiles Decision Trees to Prolog
│   ├── main.py          # Application entry point and orchestrator
│   └── ...
├── data/                # Clinical datasets (CSV)
├── prolog/              # Generated logical rules and knowledge base
├── templates/           # HTML templates for visualization
└── output/              # Query results and reasoning trees
