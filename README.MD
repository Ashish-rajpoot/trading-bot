# Delta Trader

## Overview
This project aims to develop a trading bot that interacts with the Delta Exchange platform using its API.

## Requirements

- Python 3.x
- Delta Exchange API credentials (API Key and Secret)
- `requests` library for making HTTP requests

## Installation

1. Clone the repository or download the project files.
2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. Rename `.env.example` to `.env`.
2. Update the `.env` file with your Delta Exchange API credentials:

    ```
    DELTA_API_KEY=your_api_key_here
    DELTA_API_SECRET=your_api_secret_here
    ```

## Project Structure

```
delta-trader/
├── app/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── client.py
│   │   ├── auth.py
│   │   └── endpoints.py
│   │ │   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py
│   │ │   ├── utils/
│   │   ├── __init__.py
│   │   └── logger.py
│   │ │   └── exchange/
│ ├── tests/
├── .env
├── main.py
└── requirements.txt
```

## Running the Bot

1. Ensure your environment variables are set correctly in `.env`.
2. Run the bot using the following command:

    ```bash
    python main.py
    ```
