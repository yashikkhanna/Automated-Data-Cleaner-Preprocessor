from data_ingestions import DataIngestion
from data_cleaning import DataCleaning
from ai_agent import AIAgent

DB_HOST="localhost"
DB_PORT="5432"
DB_NAME="demodb"
DB_USER="postgres"
DB_PASSWORD="Toshik@121"

DB_URL=f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

ingestion=DataIngestion(DB_URL)
cleaner=DataCleaning()
ai_agent=AIAgent()

df_csv=ingestion.load_csv("sample_data.csv")
if df_csv is not None:
    print("\n cleaning csv data...")
    df_csv=cleaner.clean_data(df_csv)
    df_csv=ai_agent.process_data(df_csv)
    print("\n AI- Cleaned CSV DATA:\n",df_csv)

df_excel=ingestion.load_excel("sample_data.xlsx")
if df_excel is not None:
    print("\n cleaning excel data...")
    df_excel=cleaner.clean_data(df_excel)
    df_excel=ai_agent.process_data(df_excel)
    print("\n AI-Cleaned excell data:\n",df_excel)

df_db=ingestion.load_from_database("SELECT * FROM my_table")
if df_db is not None:
    print("\n cleaning database data...")
    df_db=cleaner.clean_data(df_db)
    df_db=ai_agent.process_data(df_db)
    print("\n AI-Cleaned Database Data:\n",df_db)

API_URL="https://jsonplaceholder.typicode.com/posts"
df_api=ingestion.fetch_from_api(API_URL)
if df_api is not None:
    print("\n cleaning api data...")
    df_api=df_api.head(30)

if "body" in df_api.columns:
    df_api["body"]=df_api["body"].apply(lambda x:x[:100]+ "..." if isinstance(x,str) else x)

df_api=cleaner.clean_data(df_api)
df_api=ai_agent.process_data(df_api)
print("\n Ai cleaned API DATA:\n",df_api)


