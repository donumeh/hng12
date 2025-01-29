# HNG Stage Zero Task

This repo holds stage zero task of HNG Internship programme


## Task Description:

Develop a public API that returns the following information in JSON format:

* **Your registered email address** (used to register on the HNG12 slack workspace)
* **The current datetime** as an ISO 8601 formatted timestamp
* **This GitHub URL** of the project's codebase

## Requirement (used):

* **Programming Language/Framework**: Python (Flask)
* **Deployment**: On that train of thought
* **CORS Handling**: flask_cors
* **Response Format**: JSON format


## API specification
* Endpoint `GET** https://stage-zero.onrender.com`
* Required JSON Response Format (200 OK)

	```
		{
 			 "email": "your-email@example.com",
			 "current_datetime": "2025-01-30T09:30:00Z",
			 "github_url": "<https://github.com/yourusername/your-repo>"
		}
	```

## SetUp
* **Clone the repo and change directory**
		```
			git clone https://github.com/donumeh/stage_zero
			cd stage_zero
		```
* **Make sure python is installed on your device**
		```
			sudo apt install python3
		```
* **Create virtual environment for project**
		```
			python3 -m venv .venv
		```
* **Activate the virtual enviroment**
		```
			source .venv/bin/activate
		```
* **Install all project requirements with pip**
		```
			pip3 install -r requirements.txt
		```
* **Run the app**
		```
			./app.py
		```
* **Open your browser to localhost:5000**
		* (localhost:5000)[localhost:5000]

# Backlinks:
* https://hng.tech/hire/python-developers
* https://hng.tech/hire/csharp-developers
* https://hng.tech/hire/golang-developers
* https://hng.tech/hire/php-developers
* https://hng.tech/hire/java-developers
* https://hng.tech/hire/nodejs-developers


