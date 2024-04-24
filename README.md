# Wappalyzer API Integration (Website-Technology-Profiler)

## Overview
This Flask-based application allows users to analyze URLs to determine the technology stack used on those websites by leveraging the Wappalyzer API.

## Features
- URL analysis via Wappalyzer API
- Error handling for invalid or inaccessible URLs
- JSON formatted output of technology stack

## Prerequisites
- Python 3
- Flask
- Requests library

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd <project-directory>
   ```
3. Install the required Python packages:
   ```
   pip install flask requests
   ```

## Configuration
- Set your Wappalyzer API key in the `app.py` file:
  ```python
  API_KEY = 'your_api_key_here'
  ```
- The API endpoint is pre-configured as:
  ```python
  WAPPALYZER_API_ENDPOINT = 'https://api.wappalyzer.com/v2/lookup/'
  ```
- Ensure the API key and endpoint are correctly set to avoid unauthorized errors.

## Usage
- Start the server:
  ```
  python app.py
  ```
- Access the endpoint `/analyze` via GET request with a URL parameter to analyze a website:
  ```
  http://localhost:5000/analyze?url=http://example.com
  ```
- The server will return a JSON response with the technology stack or an error message.
