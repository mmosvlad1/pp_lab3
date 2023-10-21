# Flask API Project

This repository contains a simple Flask API project that responds to a specific endpoint with a "Hello World" message along with the variant number. Additionally, it includes instructions for setting up the development environment.

## Getting Started

### Prerequisites

- Python (as specified in the project requirements)
- `pip` (to install Python packages)
- `git` (for version control)

### Installation

1. Clone the repository:

   - git clone https://github.com/mmosvlad1/pp_lab3.git
   
### Create and activate a virtual environment:

python -m venv venv

#mac os
- source venv/bin/activate

#windows
- myenv\Scripts\activate


### Install the required packages:

- cd pp_lab3
- pip install -r requirements.txt

### Running the Application
Run the Flask application using a WSGI server:

- gunicorn lab3.py:app

### Testing the API Endpoint
You can test the API endpoint using the following curl command:

- curl -v -XGET http://127.0.0.1:5000/api/v1/hello-world-21