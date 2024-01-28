# Stock Transactions API

## Overview

This API is designed for managing user profiles, stock data, and transactions for a stock trading application. The API allows users to register, retrieve personal data, post and get stock data, and post and get transactions within specified parameters.

## Database Schema

### Users

| Field     | Type        | Description           |
|-----------|-------------|-----------------------|
| user_id   | Integer     | Unique identifier for the user |
| username  | String      | User's chosen name    |
| balance   | Decimal     | User's account balance |

### StockData

| Field     | Type        | Description           |
|-----------|-------------|-----------------------|
| ticker    | String      | Stock ticker symbol   |
| open_price| Decimal     | Opening price of the stock |
| close_price| Decimal    | Closing price of the stock |
| high      | Decimal     | Highest price of the day |
| low       | Decimal     | Lowest price of the day |
| volume    | Integer     | Number of shares traded |
| timestamp | Timestamp   | Time of the stock data entry |

### Transactions

| Field            | Type      | Description               |
|------------------|-----------|---------------------------|
| transaction_id   | Integer   | Unique identifier for the transaction |
| user_id          | Integer   | Identifier for the user   |
| ticker           | String    | Stock ticker symbol       |
| transaction_type | String    | Type of transaction (buy/sell) |
| transaction_volume | Integer | Number of shares transacted |
| transaction_price | Decimal | Price per share of the transaction |
| timestamp        | Timestamp | Time of the transaction entry |

## Endpoints

### User Management

- `POST /users/`: Register a new user.
- `GET /users/{username}/`: Retrieve user data.

### Stock Data

- `POST /stocks/`: Ingest new stock data.
- `GET /stocks/`: Retrieve all stock data.
- `GET /stocks/{ticker}/`: Retrieve specific stock data.

### Transactions

- `POST /transactions/`: Create a new transaction.
- `GET /transactions/{user_id}/`: Retrieve user transactions.
- `GET /transactions/{user_id}/{start_timestamp}/{end_timestamp}/`: Retrieve user transactions within a time range.

## Instructions

- Validate transactions before processing.
- Update Users and Transactions tables after each transaction.
- Document API usage, data models, and assumptions.
- Include setup instructions.

## Setup Guide

1. Clone the repository from GitHub.
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your PostgreSQL database.
4. Run migrations: `python manage.py migrate`
5. Start the server: `python manage.py runserver`

## Running Tests

- Run `python manage.py test` to execute the unit tests.

## Assumptions

- Users must have a unique username.
- Stock prices are updated in real-time.
- Users' balance cannot go below zero.
