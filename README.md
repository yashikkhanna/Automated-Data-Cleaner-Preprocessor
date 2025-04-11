✨ Project Title: AI-Based Data Cleaning and Preprocessing App
📌 Project Description:
A powerful AI-powered tool for intelligent data cleaning and preprocessing.
Users can upload messy CSV files and receive a clean, AI-processed version in return.
Optionally stores the cleaned data into a PostgreSQL database.
Uses Google Gemini API to understand and clean data based on context.
Built with FastAPI (backend) and Streamlit (frontend) for a seamless experience.

🔧 Technologies Used:
Python – Base language
FastAPI – For backend API services
Streamlit – For user interface
Pandas & NumPy – Data manipulation
Google Gemini API – AI-powered data enhancement
psycopg2 – PostgreSQL database driver
SQLAlchemy – ORM to interact with the database
dotenv – For managing environment variables
Uvicorn – ASGI server for FastAPI

🛠️ How to Run the Project
✅ Step-by-Step Guide
1.) Clone the Repository: git clone https://github.com/your-username/ai-data-cleaning-app.git
2.) Create a Virtual Environment: python -m venv ai_data_cleaning_env
3.) Activate the Virtual Environment: ai_data_cleaning_env\Scripts\activate
4.) Install Required Packages: pip install -r requirements.txt
5.)Set Up Environment Variables: Create a .env file in the root directory and add:
GOOGLE_API_KEY=your_google_gemini_api_key
DB_HOST=
DB_PORT=
DB_NAME=
DB_USER=
DB_PASSWORD=
6.) Start FastAPI Backend: uvicorn scripts.backend:app --reload
7.) Start Streamlit Frontend:streamlit run scripts/frontend.py



