from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

keyVaultName = "plant-diseases"
KVUri = f"https://{keyVaultName}.vault.azure.net"

credential = DefaultAzureCredential()
client = SecretClient(vault_url=KVUri, credential=credential)

server = 'plant-disease-test-server.database.windows.net'
database = "test"
username = "admin123"
password = '{Test123}'
driver = '{SQL SERVER}'

client.set_secret('server', server)
client.set_secret('database', database)
client.set_secret('username', username)
client.set_secret('password', password)
client.set_secret('driver', driver)

print(f"Retrieving your secret from {keyVaultName}.")

retrieved_secret = client.get_secret('username')

print(f"Your secret is '{retrieved_secret.value}'.")
