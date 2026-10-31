# API Health Monitor

A Flask-based web application that checks API availability and health by sending HTTP requests to user-provided URLs. It displays HTTP status codes, response times, reachability, and health status while maintaining a history of API checks using SQLite.

## Features

- Validate API URLs before making requests.
- Check API reachability using HTTP requests.
- Measure and display API response times.
- Distinguish between reachable and healthy endpoints.
- Handle request failures, timeouts, and HTTP error responses.
- Persist API check results using SQLite.
- View historical API checks with timestamps and status indicators.
- Display error details for unsuccessful requests.
- Automatically initialize the SQLite database when the application starts.
- Provide a responsive web interface with loading and empty states.
- Include unit tests for URL validation.

## Tech Stack

- **Language:** Python
- **Backend:** Flask
- **HTTP Client:** Requests
- **Database:** SQLite
- **Frontend:** HTML, CSS, Jinja2
- **Testing:** Python `unittest`
- **Version Control:** Git and GitHub

## Project Structure

```text
api-health-monitor/
├── app/
│   ├── __init__.py
│   ├── database.py
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

The SQLite database file (`api_health.db`) is generated automatically when the application starts and is excluded from version control.

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

The application automatically initializes the SQLite database and creates the required table if it does not already exist.

## Running Tests

Run the URL validation unit tests using:

```bash
python -m unittest discover -s tests -v
```

The tests cover URL validation scenarios, including empty URLs, unsupported schemes, local and private IP addresses, embedded credentials, missing hostnames, and valid HTTPS URLs.

## How It Works

1. Enter an API endpoint URL in the web interface.
2. The application validates the submitted URL.
3. If validation succeeds, it sends an HTTP GET request with a configured timeout.
4. The application measures response time and evaluates the HTTP response.
5. Reachability, health status, HTTP status code, response time, and error details are generated.
6. The result is saved in the SQLite database.
7. The latest API check is displayed, along with historical checks ordered from newest to oldest.

An endpoint is considered **healthy** when it returns an HTTP status code between `200` and `399`.

An endpoint can be reachable but unhealthy if it responds with an HTTP status code outside that range. If no HTTP response is received because of a timeout or connection failure, the endpoint is considered unreachable.

## Current Limitations

- API checks are triggered manually rather than running continuously.
- Historical records are displayed without pagination or filtering.
- URL validation provides basic safeguards and is not sufficient on its own for deployment as a public monitoring service.
- Automated database and route tests have not yet been implemented.

## Future Improvements

- Add pagination and filtering for historical API checks.
- Build dashboard metrics and recent-check summaries.
- Expand test coverage for HTTP requests, routes, and database operations.
- Strengthen URL validation and network-level security.
- Add scheduled monitoring and automated health checks.
- Introduce background jobs for monitoring multiple endpoints.
- Add deployment configuration and documentation.

## License
