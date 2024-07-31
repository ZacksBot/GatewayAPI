# Testing

[![Pytest](https://github.com/ZacksBot/Gateway/actions/workflows/AppTest.yml/badge.svg)](https://github.com/ZacksBot/Gateway/actions/workflows/AppTest.yml)

# Vulnerabilities API Gateway

This is a simple API gateway built using Flask. It fetches vulnerability data from the Silobreaker API converts it into a more readable gateway and and provides it in either CSV or JSON format.

### Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/ZacksBot/Gateway.git
    cd Gateway
    ```

2. **Build the Docker image**:

    ```bash
    docker build -t vulnerabilities-api-gateway .
    ```

3. **Run the Docker container**:

    ```bash
    docker run -p 5000:5000 vulnerabilities-api-gateway
    ```

    This will start the API gateway on `http://localhost:5000`.

### Usage

You can access the following endpoints:

-   **CSV Format**: `http://localhost:5000/vulnerabilities`
-   **JSON Format**: `http://localhost:5000/vulnerabilities?format=json`

## Thought Process

### Initial Approach

This task was quite simple. It required converting a lengthy URL, which was not optimal for developers, into a more accessible gateway endpoint called `/vulnerabilities`. Fetching the data from the long URL string and setting up the new endpoint was straightforward. The conversion to CSV was also simple; all I had to do was map through the JSON objects, extract specific values, and use the csv library to convert them into a `CSV` format.
