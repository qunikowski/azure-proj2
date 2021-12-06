import os
import pyodbc
from dotenv import load_dotenv
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential


load_dotenv()
KEY_VAULT_NAME = os.environ.get("keyVaultName")
KVUri = f"https://{KEY_VAULT_NAME}.vault.azure.net"

credential = DefaultAzureCredential()
client = SecretClient(vault_url=KVUri, credential=credential)

server = client.get_secret('server')
database = client.get_secret('database')
username = client.get_secret('username')
password = client.get_secret('password')
driver = client.get_secret('driver')

def add_prediction(label):
    conn = pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = conn.cursor()
    sql_insert_prediction = f"INSERT INTO Inputs (DiseaseId) VALUES ('{label}')"
    cursor.execute(sql_insert_prediction)
    cursor.commit()

def get_top_diseases(n_top, n_past_days):
    #n_past_days = 1
    #n_top = 5

    conn = pyodbc.connect('DRIVER=' + driver + ';SERVER=tcp:' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = conn.cursor()

    sql_top = f"""
    SELECT TOP {n_top} DiseaseId, COUNT (DiseaseId) AS 'count' 
    FROM Inputs 
    WHERE Date >= DATEADD(day, -{n_past_days}, GETDATE())
    GROUP BY DiseaseId 
    ORDER BY 'count' 
    DESC 
    """

    cursor.execute(sql_top)

    results=[]
    for i in cursor:
        results.append(i)

    return results






