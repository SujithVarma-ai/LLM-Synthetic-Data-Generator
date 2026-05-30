# 🚀 LLM Synthetic Data Generator

Generate high-quality synthetic datasets using local Large Language Models (LLMs) powered by Ollama.

## 📌 Overview

LLM Synthetic Data Generator is a Python-based application that generates high-quality synthetic datasets using locally hosted Large Language Models through Ollama
The application supports multiple open-source models including Llama 3.2, Gemma 3, and Qwen 2.5, allowing users to generate realistic customer reviews with sentiment labels. Generated data is displayed through an interactive Gradio interface and can be exported for machine learning, NLP, and data analysis tasks.

The project demonstrates local LLM inference, prompt engineering, synthetic data generation, dataset creation, and interactive AI application development.


## ✨ Features

* Generate synthetic customer reviews
* Automatic sentiment generation (Positive, Negative, Neutral)
* Local inference using Ollama
* Export datasets to CSV
* Interactive Gradio web interface
* Configurable number of records
* Support for multiple LLMs
    Llama 3.2
    Gemma 3
    Qwen 2.5

## 🛠️ Tech Stack

* Python
* Ollama
* Llama 3.2
* Pandas
* Gradio

## ⚙️ Installation

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

# 📸 Application Screenshot

![App Screenshot](https://github.com/SujithVarma-ai/LLM-Synthetic-Data-Generator/blob/main/Screenshot%202026-05-30%20075806.png)
![App Screenshot](https://github.com/SujithVarma-ai/LLM-Synthetic-Data-Generator/blob/main/Screenshot%202026-05-30%20075920.png)

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
