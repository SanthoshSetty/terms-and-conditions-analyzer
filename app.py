#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Required imports
from flask import Flask, render_template, request, redirect, url_for
from pdfminer.high_level import extract_text
import openai
import traceback

# Initialize Flask app
app = Flask(__name__)

# Set OpenAI API key
openai.api_key = 'YOUR-API-KEY'  # Make sure to replace with your API key

# Extract text from a PDF using pdfminer
def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)

# Concise summarization of a chunk
def concise_summarization(chunk):
    messages = [{
        "role": "system",
        "content": ("Read this terms and conditions text and Summarise any potential red flags in the text ,"
                    " especially any risks from a user safety perspective."
                    " Keep it under 100 words.")
    }, {
        "role": "user",
        "content": chunk
    }]
    
    response = openai.ChatCompletion.create(
        model="gpt-4-0613",  # Ensure this is the correct model identifier
        messages=messages,
        max_tokens=100 * 5  # assuming an average word length of 5 tokens
    )
    return response.choices[0].message['content'].strip()

# Final summarization of all chunk summaries
def final_summarization(responses):
    combined_responses = " ".join(responses)
    messages = [{
        "role": "system",
        "content": "Provide a final summary of the following summaries. Highlight what could be potential issues in terms of user safety. Format issues in bullet points"
    }, {
        "role": "user",
        "content": combined_responses
    }]
    
    response = openai.ChatCompletion.create(
        model="gpt-4-0613",  # Ensure this is the correct model identifier
        messages=messages,
        max_tokens=1024  # maximum tokens for the final summary
    )
    return response.choices[0].message['content'].strip()

# Iterative concise summarization of the content
def iterative_concise_summarization(content):
    # Tokenize the content and split into chunks of approximately 8000 tokens
    tokens = content.split()
    chunk_size = 7000
    chunks = [" ".join(tokens[i:i+chunk_size]) for i in range(0, len(tokens), chunk_size)]
    
    summaries = [concise_summarization(chunk) for chunk in chunks]
    final_summary = final_summarization(summaries)

    return final_summary

# Flask route to handle the uploaded text or PDF
@app.route('/', methods=['GET', 'POST'])
def index():
    summary = ""
    if request.method == 'POST':
        text = request.form.get('text')
        uploaded_file = request.files.get('file')
        
        if text:
            content = text
        elif uploaded_file:
            file_path = "temp_pdf.pdf"
            uploaded_file.save(file_path)
            content = extract_text_from_pdf(file_path)
        
        summary = iterative_concise_summarization(content)
        
    return render_template('index.html', summary=summary)

# Error handling
@app.errorhandler(Exception)
def handle_exception(e):
    print(traceback.format_exc())
    return "An error occurred: {}".format(e), 500

# Start Flask app in a separate thread
from threading import Thread

def run():
    app.run(use_reloader=False, port=5000)

Thread(target=run).start()


# In[ ]:




