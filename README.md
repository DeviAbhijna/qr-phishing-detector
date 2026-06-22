# QR Code Phishing Detector with Machine Learning & Deep Learning

## Project Overview

QR Code Phishing Detector is a Cybersecurity-based Web Application that analyzes QR codes and URLs to detect potential phishing attacks. The system extracts URLs from uploaded QR codes or accepts direct URL input, performs rule-based security analysis, Machine Learning prediction, Deep Learning prediction, and domain reputation checking to classify websites as Safe, Suspicious, or Phishing.

The project helps users avoid malicious websites hidden behind QR codes and demonstrates the application of Cybersecurity, Machine Learning, and Deep Learning techniques in web security.

---

## Problem Statement

QR codes are widely used for payments, login pages, advertisements, and website sharing. Attackers can create malicious QR codes that redirect users to phishing websites designed to steal credentials, banking information, or personal data.

This project aims to detect such malicious URLs before users visit them.

---

## Objectives

* Detect phishing URLs hidden inside QR codes.
* Allow direct URL analysis.
* Perform rule-based cybersecurity checks.
* Integrate Machine Learning-based phishing detection.
* Integrate Deep Learning-based phishing detection.
* Display domain reputation information.
* Maintain scan history and analytics dashboard.
* Generate security reports.

---

## Technologies Used

### Frontend

* HTML5
* CSS3
* Bootstrap 5
* JavaScript
* Chart.js

### Backend

* Python
* Flask

### Cybersecurity Components

* URL Heuristic Analysis
* Domain Reputation Checking
* QR Code Analysis

### Machine Learning

* Scikit-Learn
* Random Forest Classifier

### Deep Learning

* TensorFlow
* Keras Neural Network

### Data Handling

* Pandas
* CSV

### Additional Libraries

* OpenCV
* Pyzbar
* Validators
* ReportLab

---

## Project Architecture

User

↓

Upload QR / Enter URL

↓

URL Extraction

↓

Rule-Based Analysis

↓

Machine Learning Prediction

↓

Deep Learning Prediction

↓

Domain Reputation Check

↓

Final Verdict

↓

Dashboard & Reports

---

## Features Implemented

### 1. QR Code Scanning

* Upload QR image.
* Extract hidden URL.
* Analyze extracted URL.

### 2. Direct URL Analysis

* Users can directly enter URLs.
* No QR upload required.

### 3. Rule-Based Detection

Checks:

* HTTP instead of HTTPS
* Suspicious keywords
* Long URLs
* '@' symbols
* IP address usage

### 4. Machine Learning Detection

Random Forest model trained on phishing URL dataset.

Output:

* Benign
* Malicious

### 5. Deep Learning Detection

Neural Network trained using phishing URL dataset.

Output:

* Benign
* Malicious

### 6. Domain Reputation Checking

Displays:

* Safe
* Suspicious
* Unknown

### 7. Scan Logging

Stores:

* Timestamp
* URL
* Result

### 8. Analytics Dashboard

Displays:

* Total scans
* Safe URLs
* Suspicious URLs
* Phishing URLs
* Recent scan history
* Pie chart visualization

### 9. PDF Report Generation

Generate downloadable security reports.

---

## Dataset Used

Dataset Name:
malicious_phish.csv

Dataset Size:
651,191 URLs

Classes:

* Benign
* Phishing
* Malware
* Defacement

Sample Data:

br-icloud.com.br → Phishing

mp3raid.com/music/krizz_kaliko.html → Benign

garage-pirenne.be → Defacement

---

## Project Folder Structure

qr_phishing_detector/

│

├── app.py

├── qr_reader.py

├── url_checker.py

├── reputation_checker.py

├── ml_model.py

├── dl_model.py

├── train_model.py

├── train_dl_model.py

├── scan_logger.py

├── report_generator.py

├── scan_logs.csv

│

├── uploads/

│

├── phishing_dataset/

│   └── malicious_phish.csv

│

├── templates/

│   ├── index.html

│   └── dashboard.html

│

└── static/

---

## Example Test URLs

### Safe URLs

https://google.com

https://www.wikipedia.org

https://github.com

https://www.microsoft.com

### Suspicious URL

https://secure-login.example.com

### Phishing URL

http://secure-login-update-bank.com

---

## Detection Workflow

Step 1:
User uploads QR code or enters URL.

Step 2:
URL extracted.

Step 3:
Rule-Based Analysis performed.

Step 4:
Machine Learning prediction generated.

Step 5:
Deep Learning prediction generated.

Step 6:
Domain reputation checked.

Step 7:
Final verdict displayed.

Step 8:
Scan stored in dashboard logs.

---

## Advantages

* Prevents phishing attacks.
* Detects malicious URLs before visiting.
* Combines Cybersecurity + AI.
* Real-world security application.
* Useful for academic projects and placements.
* Demonstrates Flask, ML, DL, and Cybersecurity skills.

---

## Future Enhancements

* Real-time camera QR scanning.
* Google Safe Browsing API.
* VirusTotal API Integration.
* WHOIS lookup.
* Domain age verification.
* PostgreSQL database integration.
* User authentication system.
* Email alerts.
* Threat intelligence feeds.
* Advanced analytics dashboard.
* Cloud deployment on AWS.
* Mobile application support.

---

## Academic Relevance

Domains Covered:

* Cybersecurity
* Web Security
* Machine Learning
* Deep Learning
* Data Analytics
* Full Stack Development

This project demonstrates practical implementation of Cybersecurity concepts combined with AI-based threat detection techniques, making it suitable for academic reviews, internships, placements, and final-year project presentations.

---

## Developed By

Abhijna Marisetti

B.Tech Computer Science and Engineering

Shri Vishnu Engineering College for Women

Project Domain:
Cybersecurity + Machine Learning + Deep Learning
<img width="377" height="568" alt="image" src="https://github.com/user-attachments/assets/d5df46a9-ea65-4932-9413-6954e3f8f62f" />
<img width="892" height="589" alt="image" src="https://github.com/user-attachments/assets/9c863675-feb0-40c3-888b-74405bd34973" />
<img width="619" height="428" alt="image" src="https://github.com/user-attachments/assets/4d4bd57f-3b48-4701-bf50-b0a9196199bd" />
![Uploading image.png…]()



