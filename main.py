from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (good for local development)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],
)

def fetch_sales_from_db():
    conn = sqlite3.connect('sales_database.db')
    cursor = conn.cursor()
    
    # SQL Query: Select all records
    cursor.execute("SELECT * FROM sales_table")
    rows = cursor.fetchall()
    
    # Get column names
    column_names =[desc[0] for desc in cursor.description]
    conn.close()
    
    # Combine column names with row data to create a Dictionary (JSON format)
    result =[dict(zip(column_names, row)) for row in rows]
    return result

# 1. Root Endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Sales API"}

# 2. Sales Endpoint
@app.get("/sales")
def get_sales():
    data = fetch_sales_from_db()
    return {"sales_data": data}

# --- AI ENGINEERING PART ---

# A mock function to simulate an LLM (Large Language Model) like ChatGPT
def call_llm_agent(prompt: str):
    # In reality, this is where we do: openai.ChatCompletion.create(prompt=prompt...)
    print(f"--- SENDING PROMPT TO AI ---\n{prompt}\n----------------------------")
    
    # Simulating AI logic based on keywords
    if "Laptop" in prompt:
        return "AI Insight: Laptops are generating the highest revenue. Recommendation: Increase your marketing budget for Laptops and create bundle deals with Keyboards to boost sales further."
    else:
        return "AI Insight: Sales are steady. Keep monitoring inventory."

# 3. AI Insights Endpoint
@app.get("/ai-insights")
def get_ai_insights():
    # 1. Fetch raw data
    data = fetch_sales_from_db()
    
    # 2. Process data to feed the AI (Problem Solving / DSA logic)
    # We create a dictionary to sum revenues per product
    revenue_by_product = {}
    for item in data:
        prod = item["Product"]
        rev = item["TotalRevenue"]
        # If product exists, add to it. If not, start at 0 and add.
        revenue_by_product[prod] = revenue_by_product.get(prod, 0) + rev
        
    # Find the product with the maximum revenue
    best_product = max(revenue_by_product, key=revenue_by_product.get)
    
    # 3. PROMPT ENGINEERING
    # We inject our real data into a natural language prompt
    prompt = f"Hello AI. Here is my sales summary: {revenue_by_product}. The best seller is {best_product}. What is your business recommendation for next month?"
    
    # 4. Call the AI
    ai_response = call_llm_agent(prompt)
    
    # 5. Return the full intelligence to the Frontend
    return {
        "sales_summary": revenue_by_product,
        "best_seller": best_product,
        "ai_recommendation": ai_response
    }