## 🧠 Smart Sentiment Analyzer

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/Framework-Flask-orange.svg" alt="Flask">
  <img src="https://img.shields.io/badge/ML%20Model-Hugging%20Face-yellow.svg" alt="Hugging Face">
  <img src="https://img.shields.io/badge/Cloud-Google%20Cloud%20Run-blueviolet.svg" alt="GCP">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
</p>

A modern, production-ready web application that utilizes advanced Natural Language Processing (NLP) to perform real-time sentiment analysis. Built with **Flask** and the **Hugging Face `distilbert-base-uncased-finetuned-sst-2-english`** model, this application is containerized with Docker and deployed as a scalable service on Google Cloud Run.

## 🚀 Features

- **Deep Learning Inference:** Leverages a fine-tuned Transformer model to classify text sentiment with high accuracy and confidence scoring.
- **Production-Grade Backend:** Employs an application factory pattern with multi-threaded Gunicorn workers for reliable concurrent processing.
- **Cinematic & Responsive UI:** Designed with a warm vintage aesthetic using Bootstrap 5, featuring a dynamic loading state and results visualization.
- **Scalable Infrastructure:** Dockerized and prepared for serverless deployment on Google Cloud Run.

---

## 🏗️ Project Architecture

```text
sentiment-analyzer/
├── app/
│   ├── __init__.py          # Application Factory
│   ├── analyzer.py          # Hugging Face pipeline initialization
│   ├── routes.py            # REST API endpoint definitions
│   ├── static/
│   │   └── css/
│   │       └── style.css    # Custom warm-sepia styling
│   └── templates/
│       ├── base.html        # Main layout wrapper
│       └── index.html       # Dynamic AJAX interface
├── Dockerfile               # Production multi-stage container build
├── requirements.txt         # Dependencies
├── run.py                   # Application entry point
└── README.md
```

## 🛠️ Tech StackCore: Python, Flask, GunicornMachine Learning: PyTorch, Hugging Face transformersFrontend: Bootstrap 5, JavaScript (AJAX), HTML5, CSS3DevOps & Cloud: Docker, Google Cloud Platform (Cloud Run)💻 Local Installation and Setup1. Clone the RepositoryBashgit clone [https://github.com/YOUR_GITHUB_USERNAME/sentiment-analyzer.git](https://github.com/YOUR_GITHUB_USERNAME/sentiment-analyzer.git)
cd sentiment-analyzer

2. Install DependenciesIt is recommended to use a Python virtual environment:Bashpython3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt

4. Run the Application LocallyBashpython run.py
The application will be accessible at http://localhost:8080.☁️ Deployment to Google Cloud RunInitialize the Google Cloud SDK and log in:Bashgcloud auth login
gcloud config set project YOUR_PROJECT_ID

Build and deploy to your preferred region (e.g., asia-south1 for optimal latency):Bashgcloud run deploy sentiment-analyzer \
    --source . \
    --region asia-south1 \
    --allow-unauthenticated \
    --min-instances 0 \
    --max-instances 2 \
    --memory 2Gi
---
    
## 🧪 Usage ExamplesTest the endpoint with these sample inputs to observe classification and confidence scores:Input TextExpected LabelConfidence"This is the best application I have ever used, it works flawlessly!"POSITIVE> 95%"The deployment process was incredibly smooth and saved us a lot of time."POSITIVE> 90%"The application crashed immediately when I tried to run it."NEGATIVE> 99%🤝 ContributingContributions are welcome! Feel free to open an issue or submit a pull request if you have ideas for model optimization or UI enhancements.📄 LicenseDistributed under the MIT License. See LICENSE for more information.
