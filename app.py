
# Step 1: Import Required Libraries
import requests
from PIL import Image
from transformers import pipeline
import gradio as gr
import re  # Import regular expressions module for case-insensitive keyword matching


# Step 2: Define a Function to Perform OCR
def perform_ocr(image):
    ocr_pipeline = pipeline("image-to-text", model="microsoft/trocr-base-handwritten")
    extracted_text = ocr_pipeline(image)
    return extracted_text[0]['generated_text'] if extracted_text else ""


# Step 3: Define Function to Highlight Keyword
def highlight_keyword(text, keyword):
    if not keyword:  # Check if the keyword is empty
        return "No keyword was entered."
    
    # Ensure case-insensitivity while highlighting (preserving original casing)
    keyword_pattern = re.compile(re.escape(keyword), re.IGNORECASE)  # Create case-insensitive pattern
    
    # Check if the keyword exists in the text
    if keyword_pattern.search(text):
        highlighted_text = keyword_pattern.sub(lambda match: f"<mark>{match.group(0)}</mark>", text)
        return highlighted_text
    else:
        return f"Keyword '{keyword}' not found in the extracted text."


# Step 4: Define Gradio Interface Function
def ocr_and_highlight(image, keyword):
    extracted_text = perform_ocr(image)
    keyword_result = highlight_keyword(extracted_text, keyword)
    return extracted_text, keyword_result


# Step 5: Create Gradio Interface
interface = gr.Interface(
    fn=ocr_and_highlight,
    inputs=[
        gr.Image(type="pil", label="Upload Image"),
        gr.Textbox(label="Enter Keyword (optional)")
    ],
    outputs=[
        gr.Textbox(label="Extracted Text", interactive=False),
        gr.HTML(label="Keyword Result")  # Changed to HTML to allow highlighting
    ],
    title="OCR Text Extractor with Keyword Highlighting",
    description="Upload an image to extract text and highlight a specified keyword. If no keyword is entered, the app will notify you."
)


# Step 6: Launch the Gradio Interface
interface.launch(share=True)
