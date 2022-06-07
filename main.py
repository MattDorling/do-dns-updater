from time import sleep
import requests
import config
import logging

logging.basicConfig(level=logging.INFO)


def get_public_ip():
    return requests.get('https://api.ipify.org').text


def update_dns(new_ip):
    logging.info("Fetching record ID from DigitalOcean API...")
    response = requests.get(f'https://api.digitalocean.com/v2/domains/{config.DOMAIN_NAME}/records/',
                            headers={
                                "Authorization": f"Bearer {config.DO_API_TOKEN}"},
                            params={
                                'name': config.NAME + '.' + config.DOMAIN_NAME,
                                'type': config.TYPE,
                            })

    domain_record_id = response.json()['domain_records'][0]['id']

    logging.debug(f"Record ID: {domain_record_id}")

    logging.info("Updating IP through DigitalOcean API")
    response = requests.patch(f'https://api.digitalocean.com/v2/domains/{config.DOMAIN_NAME}/records/{domain_record_id}/',
                              headers={
                                  "Authorization": f"Bearer {config.DO_API_TOKEN}"},
                              json={
                                  'name': config.NAME,
                                  'type': config.TYPE,
                                  'data': str(new_ip)
                              })
    logging.debug(f"Response: {response}")


ip = get_public_ip()
logging.info(f"Initial IP address is {ip}")

update_dns(ip)

logging.info(f"Waiting for the public IP to change...")
while True:
    new_ip = get_public_ip()
    if new_ip != ip:
        update_dns(new_ip)
        logging.info(f"Waiting for the public IP to change...")
        ip = new_ip
    sleep(config.PUBLIC_IP_CHECK_INTERVAL)
