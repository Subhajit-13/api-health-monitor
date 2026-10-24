# API Health Monitor

A Flask-based web application that checks API availability and health by sending HTTP requests to a user-provided URL. It displays the HTTP status code, response time, and whether the endpoint is reachable and healthy.

## Features

- Validate API URLs before making requests.
- Check API reachability using HTTP requests.
- Display HTTP status codes and response times.
- Distinguish between reachable and healthy endpoints.
- Handle request failures and display error messages.
- Provide a responsive web interface built with HTML and CSS.
- Include unit tests for URL validation.

## Tech Stack

- **Language:** Python
- **Backend:** Flask
- **HTTP Client:** Requests
- **Frontend:** HTML, CSS, Jinja2
- **Testing:** Python `unittest`
- **Version Control:** Git and GitHub

## Project Structure

```text
api-health-monitor/
├── app/
│   ├── __init__.py
│   ├── monitor.py
│   ├── routes.py
│   ├── static/
│   │   └── style.css
│   └── templates/
│       └── index.html
├── tests/
│   └── test_monitor.py
├── .gitignore
├── requirements.txt
├── README.md
└── run.py
```

## Getting Started

### Prerequisites

- Python 3.10 or later
- pip

### 1. Clone the Repository

```bash
git clone https://github.com/Subhajit-13/api-health-monitor.git
cd api-health-monitor
```

### 2. Create and Activate a Virtual Environment

On macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python run.py
```

Open the following URL in your browser:

```text
http://127.0.0.1:5000
```

## Running Tests

Run the URL validation unit tests using:

```bash
python -m unittest discover -s tests -v
```

The tests cover URL validation scenarios, including empty URLs, unsupported schemes, local and private IP addresses, embedded credentials, missing hostnames, and valid HTTPS URLs.

## How It Works

1. Enter an API endpoint URL in the web interface.
2. The application validates the submitted URL.
3. If validation succeeds, it sends an HTTP request with a configured timeout.
4. The application measures response time and evaluates the HTTP status code.
5. The result is displayed with reachability, health status, response time, and any applicable error message.

An endpoint is considered **healthy** when it returns an HTTP status code between `200` and `399`. An endpoint may be reachable but unhealthy if it returns another HTTP status code.

## Current Limitations

- Check results are not persisted between application restarts.
- Historical check records and scheduled monitoring are not yet implemented.
- URL validation provides basic safeguards and is not sufficient on its own for deployment as a public monitoring service.
- The application currently checks endpoints on demand rather than monitoring them continuously.

## Future Improvements

- Persist API check results using SQLite.
- Display historical checks with timestamps.
- Add dashboard metrics and recent-check summaries.
- Expand test coverage for HTTP requests, routes, and database operations.
- Strengthen URL validation and network-level security.
- Add scheduled monitoring and automated health checks.
- Add deployment configuration and documentation.

## License

No license has been specified yet.
