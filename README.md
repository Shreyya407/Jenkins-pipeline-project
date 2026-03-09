# Jenkins Automated Build Pipeline Project

## Project Overview

This project demonstrates a simple **CI (Continuous Integration) pipeline** using Jenkins.
The pipeline automatically pulls source code from GitHub and executes a Python application through defined pipeline stages.

The application implemented in this project is a **Password Strength Checker** written in Python.

---

## Tools and Technologies Used

* Jenkins – Automation server for building pipelines
* GitHub – Source code repository
* Python – Programming language used for the application
* Visual Studio Code – Code editor used for development
* Git – Version control system

---

## Project Structure

```
jenkins-pipeline-project
│
├── app.py
├── Jenkinsfile
└── README.md
```

---

## Application Description

The Python application checks the strength of a password using the following criteria:

* Minimum length of 8 characters
* Presence of uppercase letters
* Presence of lowercase letters
* Presence of digits
* Presence of special characters

Based on these conditions, the password is classified as:

* Strong Password
* Medium Password
* Weak Password

---

## Jenkins Pipeline Stages

The Jenkins pipeline consists of the following stages:

1. Checkout Code
   Jenkins retrieves the source code from the GitHub repository.

2. Build
   Jenkins prepares the application environment.

3. Run Application
   Jenkins executes the Python program to check password strength.

---

## Pipeline Workflow

```
Developer Pushes Code to GitHub
           ↓
Jenkins Fetches Repository
           ↓
Pipeline Executes Jenkinsfile
           ↓
Build Stage Runs
           ↓
Python Application Executes
```

---

## Output Example

```
Building application
Password Strength Checker
Password: DevOps123!
Strength: Strong Password
```

---

## Conclusion

This project demonstrates how Jenkins can be used to automate application execution using pipelines.
By integrating GitHub with Jenkins, the process of building and running applications becomes automated, enabling continuous integration.

---

## Author

Shreya
DevOps Mini Project – Jenkins Pipeline
