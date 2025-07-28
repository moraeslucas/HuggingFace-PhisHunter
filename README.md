---
title: PhishHunter
emoji: 🕵️‍♂️
colorFrom: blue
colorTo: indigo
sdk: gradio
#sdk_version: "{{sdkVersion}}"
app_file: app.py
pinned: false
---

\# PhishHunter 



PhishHunter is an open-source NLP-based email classification tool that detects phishing attempts and explains why an email might be suspicious.



\## 🔧 Technologies Used



\- \[Hugging Face Transformers](https://huggingface.co/)

\- \[Gradio](https://gradio.app/)

\- \[NLTK](https://www.nltk.org/)

\- \[YAKE](https://github.com/LIAAD/yake)

\- \[LangDetect](https://pypi.org/project/langdetect/)

\- \[extract-msg](https://pypi.org/project/extract-msg/)

\- Python 3.8+



> \*\*Note:\*\* Although `spaCy` is listed in requirements, it is not actively used in the codebase.



\## 🚀 Getting Started



1\. Clone the repository or download the project folder:



&nbsp;  ```bash

&nbsp;  git clone https://github.com/SEU\_UTILIZADOR/phishhunter.git

&nbsp;  cd phishhunter

&nbsp;  ```



2\. Create and activate a virtual environment:



&nbsp;  ```bash

&nbsp;  python -m venv venv

&nbsp;  venv\\Scripts\\activate    # Windows

&nbsp;  # ou

&nbsp;  source venv/bin/activate  # Linux/macOS

&nbsp;  ```



3\. Install dependencies:



&nbsp;  ```bash

&nbsp;  pip install -r requirements.txt

&nbsp;  ```



4\. Run the app:



&nbsp;  ```bash

&nbsp;  python app\_improved.py

&nbsp;  ```



\## 📦 Features



\- Classify email text using a fine-tuned BERT model

\- Heuristic-based rules per language (via `rules.yaml`)

\- Language detection for multilingual support

\- Keyword extraction

\- URL verification via VirusTotal API

\- Gradio-based interface for easy use



---



\## 📜 License



This project is licensed under the MIT License.

