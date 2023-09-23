import joblib
import warnings
import sklearn
import gradio as gr
from utils import *

warnings.filterwarnings('ignore')



def predict(text):
  text = [text]
  model = joblib.load('model.pkl')
  return str(model.predict(text))

widget_text = gr.inputs.Textbox(label="Enter the text")
demo = gr.Interface(
    fn=predict,
    inputs=widget_text,
    outputs="text",
    title = "Classifier of Positive and Negative Movie Reviews"
)

if __name__ == "__main__":

  demo.launch()
