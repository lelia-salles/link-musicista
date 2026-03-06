import os, time, requests

def update_hostoo():
    token = os.getenv('API_TOKEN')
    sub = os.getenv('SUBDOMAIN')
    try:
        meu_ip = requests.get('https://api.ipify.org').text
        # Endpoint de atualização da Hostoo (exemplo)
        url = f"https://api.hostoo.com.br/v1/domains/{sub}/dns"
        headers = {"Authorization": f"Bearer {token}"}
        requests.put(url, json={"type": "A", "content": meu_ip}, headers=headers)
        print(f"Sucesso! Hostoo apontando para {meu_ip}")
    except Exception as e:
        print(f"Erro na sincronia: {e}")

while True:
    update_hostoo()
    time.sleep(600) # Atualiza a cada 10 minutos