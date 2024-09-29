---
title: OCR Model
emoji: 🦀
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: 4.44.0
app_file: app.py
pinned: false
short_description: This Model helps to extract text from inputed images.
---

# OCR Web Application

This is a basic web application built using Gradio and Hugging Face Transformers to demonstrate Optical Character Recognition (OCR). The application can extract text from single line images in english language and highlight specified keywords.
However, a lot of work needs to be done on this such as supporting multiple languages and extracting paragraphs from images.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Running the Application Locally](#running-the-application-locally)
- [Deployment Process](#deployment-process)
- [Model Description](#model-description)

## Prerequisites

Make sure you have the following installed on your machine:

- Python 3.6 or higher
- pip (Python package installer)

## Setup Instructions

1. **Clone the Repository**:

   Clone this repository to your local machine using the following command:

   git clone <repository-url>
   cd <repository-name>
   
2. **Create the virtual environment**:


   python -m venv ocr-env <br>
   source ocr-env/bin/activate  # On Windows use `ocr-env\Scripts\activate`


3. **Install the Required Libraries**:

   pip install -r requirements.txt


## Running the Application locally
To run the web application on your local machine, execute the following command in your terminal:

python app.py

## Deployment Process

Once I was satisfied with the functionality of my web application, I decided to deploy it to make it accessible to others. Here’s how I did it:

**1. Choose a Deployment Platform**: I opted for Hugging Face Spaces because it allows easy deployment for machine learning applications. However, other platforms like Streamlit Sharing or Heroku could also work.

**2. Clone the Repository**: First, I cloned my project repository from GitHub or any other version control platform I was using. This ensured I had all the latest code on my local machine.

git clone https://github.com/username/OCR_Model.git

**3. Set Up Environment Variables**: If my application required any sensitive information or API keys, I made sure to set those up in environment variables on the deployment platform.

**4. Requirements File**: I created a requirements.txt file that listed all the necessary libraries:

-gradio<br>
-transformers<br>
-Pillow<br>
-requests<br>
-torch<br>
-tensorflow<br>
-tf-keras<br>

This file would ensure that the platform installs all the dependencies needed to run the application.

**5. Deployment Configuration**: On Hugging Face Spaces, I navigated to the "Create a Space" option and selected the "Gradio" template. I uploaded my code as app.py and the requirements.txt file to the space. The platform automatically detects the required libraries and installs them.

**6. Running the Application**: After the upload, I clicked on the "Run" button. The Hugging Face platform handles the execution of my application. I could see real-time logs, which helped in debugging if anything went wrong during the startup process.

**7. Testing**: Once the application was running, I accessed the URL provided by Hugging Face to test its functionality. I made sure everything was working as expected before sharing it with others.

**8. Sharing**: After confirming that the application was live and functional, I shared the link with friends, colleagues, and any potential users to gather feedback and improve the application.

By following these steps, I successfully deployed my web application, making it accessible for anyone interested in using my OCR model.

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.








Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
