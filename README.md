# DigitalOcean DNS Updater
Simple Python script for updating DigitalOcean DNS through their API, that can easily run in a Docker container. An alternative to using Dynamic DNS.

## How to use

### Install and configure
```bash
# clone the repo
git clone https://github.com/MattDorling/do-dns-updater

# go into the directory
cd do-dns-updater

# create the config file and enter your settings
cp config.example.yml config.yml
nano config.yml

# create the .env file and enter your DigitalOcean auth token
cp example.env .env
nano .env
```

### Run

#### Option A: Docker Compose
> Assuming [Docker](https://docs.docker.com/engine/install/) and [Docker Compose](https://docs.docker.com/compose/install/) are already installed
```bash
docker-compose up
```

#### Option B: Local
```bash
# install requirements
pip3 install -r requirements.txt

# run Python script
python3 ./main.py
```

## To do
This is a very simple script that may not be changed much as it works for what I need it for.
However there are some potential future improvements: 
 - update multiple DNS records (currently it only updates one)
 - checking the DNS records on DigitalOcean
 - error handling

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
