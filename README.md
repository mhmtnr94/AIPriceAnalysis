# 🚀 AI-Powered Sales Analytics Dashboard

A full-stack, data-driven web application that processes raw sales data, stores it in a SQL database, exposes it via a fast backend, and provides AI-generated business insights on a modern frontend.

## 🌟 Project Overview

This project demonstrates an end-to-end data pipeline and web architecture. It takes "dirty" Excel data, cleans it using Python and Pandas, serves it through FastAPI, generates business insights using AI Engineering techniques, and visualizes everything on a reactive UI built with React and Tailwind CSS v4.

## 🛠️ Core Tech Stack

**Data & Backend:**
*   **Python:** Core logic and data manipulation.
*   **Pandas:** Data cleaning, feature engineering, and aggregation.
*   **SQLite:** Lightweight relational database for data storage.
*   **FastAPI:** High-performance RESTful API creation.

**Frontend:**
*   **React (Vite):** Fast, component-based UI development.
*   **Tailwind CSS v4:** Utility-first CSS framework for rapid and modern styling (zero-config setup).

**Other Skills Showcased:**
*   **AI Engineering:** Processing data into prompts to simulate an LLM (Large Language Model) agent for business insights.
*   **Data Structures & Algorithms (DSA):** Implementing real-time search and filtering logic on the client side (`O(N)` time complexity).

---

## ⚙️ Architecture & Data Flow

1.  **Data Ingestion:** Reads raw sales data from an Excel file (`sales.xlsx`).
2.  **Data Cleaning:** Filters out invalid records (e.g., negative quantities) and handles missing values using Pandas.
3.  **Storage:** Automatically provisions a SQLite database (`sales_database.db`) and saves the cleaned data.
4.  **API Layer:** FastAPI serves the data and an AI-processed summary to the frontend via `/sales` and `/ai-insights` endpoints.
5.  **Client UI:** React consumes the API and displays a modern dashboard with real-time search capabilities.

---

## 🚀 How to Run the Project Locally

### Prerequisites
*   [Python 3.x](https://www.python.org/)
*   [Node.js](https://nodejs.org/)

### 1. Backend Setup
Navigate to the root directory and install the required Python packages:
```bash
pip install pandas openpyxl fastapi uvicorn

First, run the data analysis script to clean the data and build the SQL database:
python analysis.py

Then, start the FastAPI server:
uvicorn main:app --reload
The API will be available at http://127.0.0.1:8000

2. Frontend Setup
Open a new terminal window, navigate to the frontend directory, and install the dependencies:
cd frontend
npm install

Start the Vite development server:
npm run dev
The React app will be available at http://localhost:5173

