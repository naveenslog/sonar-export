  SonarQube Data Scraper Documentation body { font-family: Arial, sans-serif; }

SonarQube Data Scraper
======================

Scrapes data from a SonarQube instance's web interface and exports the findings to an Excel file.

Table of Contents
-----------------

*   [Prerequisites](#prerequisites)
*   [Setup](#setup)
*   [Usage](#usage)
*   [Features](#features)
*   [Contributing](#contributing)
*   [License](#license)

Prerequisites
-------------

*   Python 3.6 or higher
*   Virtual environment (recommended)

Setup
-----

1.  **Clone the Repository:**  
    Clone this repository to your local machine.
    
        git clone [repository-url]
        cd [repository-dir]
    
2.  **Virtual Environment Setup:**  
    Set up and activate a Python virtual environment:
    
        python -m venv venv
    
    For **Windows**:
    
        .\venv\Scripts\activate
    
    For **macOS and Linux**:
    
        source venv/bin/activate
    
3.  **Install Dependencies:**  
    Install the required packages listed in `requirements.txt`:
    
        pip install -r requirements.txt
    
4.  **Environment Configuration:**  
    Copy `template.env` to a new file named `.env`. Update this `.env` file with your SonarQube instance details and credentials:
    
        cp template.env .env
    

Usage
-----

To run the scraper:

1.  Execute the main script:  
    
        python main.py
    
2.  Upon successful execution, an Excel file named after your project (e.g., `hdb-backend-lo.xlsx`) will be created in the current directory, containing the scraped data.

Features
--------

*   **Login Automation:** Logs into a SonarQube instance using provided credentials.
*   **Project Navigation:** Directly navigates to the issues page of the specified project.
*   **Data Extraction:** Automatically scrolls, clicks "Show More" to ensure all issues are loaded, and then extracts details like filepath, issue description, line number, type, criticality, and effort.
*   **Excel Export:** Effortlessly exports the scraped data into an Excel file format for further analysis.

Contributing
------------

Contributions are welcome! If you're looking to make larger changes or significant additions, please open an issue first to discuss your proposed changes. This ensures that your improvements align with the project's direction and desired enhancements.

License
-------

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).