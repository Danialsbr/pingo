# Network Monitoring and Discovery

## Description
This project is a web-based system for network monitoring and discovery. It allows users to monitor the status of network devices and perform network scans to discover devices within a given IP range. The application is built using Python and the Flask web framework.

## Requirements
To use this project, you will need to have the following installed:

- Python
- Flask
- SQLite

## Getting Started
To get started with this project, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies listed in `requirements.txt`.
3. Set up a virtual environment (optional but recommended).
4. Run the `app.py` file to start the Flask server.
5. Access the application through the provided URL.

## Project Structure
The project follows the following structure:

- `app.py`: The main Flask application file containing the routes and view functions.
- `templates/`: Directory containing HTML templates.
  - `base.html`: The base HTML template that other templates extend.
  - `index.html`: The home page template that extends `base.html`.
  - `status.html`: The status page template that extends `base.html`.
  - `logs.html`: The logs page template that extends `base.html`.
  - `scanning.html`: The network scanning page template that extends `base.html`.
- `static/`: Directory containing static files.
  - `css/`: Directory containing CSS stylesheets.
    - `style.css`: Custom CSS styles for the application.
  - `js/`: Directory containing JavaScript files.
    - `script.js`: Custom JavaScript code for the application.
- `devices.txt`: Text file containing a list of network devices and their IP addresses.
- `log.db`: SQLite database file to store logs of device statuses.

## Usage
- Access the home page to view the status of network devices.
- Navigate to the Status page to see the current status of all devices.
- Click on a device's IP address to view its detailed logs.
- Access the Scanning page to perform network scanning and discovery by providing an IP range.

## Resources
- Flask: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
- SQLite: [https://www.sqlite.org/docs.html](https://www.sqlite.org/docs.html)




