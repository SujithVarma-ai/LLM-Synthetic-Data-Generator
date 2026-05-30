# 🚀 LLM Synthetic Data Generator

Generate high-quality synthetic datasets using local Large Language Models (LLMs) powered by Ollama.

## 📌 Overview

This project generates synthetic datasets such as customer reviews and sentiment labels using local LLMs like Llama 3.2. The generated data is stored in a structured format using Pandas DataFrames and can be exported as CSV files for machine learning, data analysis, and experimentation.

## ✨ Features

* Generate synthetic customer reviews
* Automatic sentiment generation (Positive, Negative, Neutral)
* Local inference using Ollama
* Export datasets to CSV
* Interactive Gradio web interface
* Configurable number of records
* Support for multiple LLMs

## 🛠️ Tech Stack

* Python
* Ollama
* Llama 3.2
* Pandas
* Gradio

## ⚙️ Installation

Clone the repository:

Install dependencies:

```bash
pip install -r requirements.txt
```

Install and run Ollama:

```bash
ollama run llama3.2
```

## ▶️ Run the Application

```bash
python app.py
```

Launch the Gradio interface and generate synthetic datasets.

## 📊 Sample Output

| Review                              | Sentiment |
| ----------------------------------- | --------- |
| Great product and fast delivery.    | Positive  |
| Customer support was unhelpful.     | Negative  |
| The experience was average overall. | Neutral   |

## 🎯 Future Enhancements

* Support for FAQs dataset generation
* Support for Support Ticket datasets
* Multiple language support
* Industry-specific dataset generation
* Export to JSON and Excel
* Advanced prompt customization
