from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

KVUri = "https://plant-disease-detector.vault.azure.net"
credential = DefaultAzureCredential()
client = SecretClient(vault_url=KVUri, credential=credential)

DATABASE_URL = client.get_secret('DATABASE-URL').value
PREDICTOR_URL = client.get_secret('PREDICTOR-URL').value
PREDICTION_KEY = client.get_secret('PREDICTION-KEY').value

