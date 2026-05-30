import gradio as gr
import pandas as pd

def show_dataset(dataset_type, model, num_records):
    df = pd.read_csv("synthetic_reviews.csv")
    return df
gr.Interface(
    fn=show_dataset,
    inputs=[
        gr.Dropdown(
            ["Sentiment Analysis"],
            label="Dataset Type"
        ),
        gr.Dropdown(
            ["llama3.2", "qwen2.5", "gemma3"],
            label="Model"
        ),
        gr.Number(
            label="Number of Records",
            value=100
        )
    ],
    outputs=gr.Dataframe()
).launch()
