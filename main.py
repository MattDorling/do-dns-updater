from time import sleep
import requests
import config


def get_public_ip():
    return requests.get('https://api.ipify.org').text


def update_dns(new_ip):
    response = requests.get(f'https://api.digitalocean.com/v2/domains/{config.DOMAIN_NAME}/records/',
                            headers={
                                "Authorization": f"Bearer {config.DO_API_TOKEN}"},
                            params={
                                'name': config.NAME + '.' + config.DOMAIN_NAME,
                                'type': config.TYPE,
                            })

    domain_record_id = response.json()['domain_records'][0]['id']

    response = requests.patch(f'https://api.digitalocean.com/v2/domains/{config.DOMAIN_NAME}/records/{domain_record_id}/',
                              headers={
                                  "Authorization": f"Bearer {config.DO_API_TOKEN}"},
                              json={
                                  'name': config.NAME,
                                  'type': config.TYPE,
                                  'data': str(new_ip)
                              })
    print(response)


ip = get_public_ip()
update_dns(ip)

while True:
    new_ip = get_public_ip()
    if new_ip != ip:
        update_dns(new_ip)
        ip = new_ip
    print('My public IP address is: {}'.format(ip))
    sleep(config.PUBLIC_IP_CHECK_INTERVAL)
