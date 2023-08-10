# Terms & Conditions Analyzer

**Terms & Conditions Analyzer**: A web tool leveraging OpenAI's GPT-4 to simplify and highlight risks in Terms & Conditions. Users can paste text or upload PDFs to receive user-focused summaries, making legal content more accessible.

## Setup

1. **Clone the Repository**:

git clone https://github.com/SanthoshSetty/terms-and-conditions-analyzer.git
cd terms-and-conditions-analyzer

2. **Install the Required Packages**:

pip install -r requirements.txt


3. **Set Your OpenAI API Key**:
Set it by using an environment variable:

export OPENAI_API_KEY='YOUR_API_KEY'


4. **Run the Flask App**:

python app.py


5. **Access the Web Application**:
Open your browser and navigate to `http://127.0.0.1:5000/` to use the application.

## Usage

- Paste the text of the terms & conditions into the provided text area OR upload a PDF containing the terms & conditions.
- Click "Analyze" to receive a concise summary of the content.

