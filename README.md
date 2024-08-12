# Flask Data Retrieval and Processing System

## Description

This Flask application simulates a simplified version of a data retrieval and processing system with endpoints for fetching, processing, and retrieving data.

## Features

1. *API Endpoint for Data Retrieval:*
   - **GET /fetch-data**: Simulates fetching data from an external service.
2. *Data Processing:*
   - **POST /process-data**: Processes the fetched data by converting all text to uppercase and stores it in memory.
3. *Data Storage:*
   - Simulates storing the processed data in an in-memory dictionary.
4. *API Endpoint for Processed Data:*
   - **GET /get-processed-data**: Returns the processed data stored in memory.

## Setup and Running Locally

1. *Clone the Repository:*
   ```bash
   git clone <repository-url>
   cd <repository-directory>
