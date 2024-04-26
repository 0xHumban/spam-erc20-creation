#!/usr/bin/python3

from brownie import *
import os
import json
from datetime import datetime, time
import random
import time



def write_in_file(filepath, data):
    with open(filepath, 'w') as outfile:
        json.dump(data, outfile)

def load_filepath(config):
    # load file configs
    dirpath = str(config['outputfile']['dirpath'])
    json_filename = str(config['outputfile']['json_filename'])
    
    # get the current date
    now = datetime.now()
    date_time_str = now.strftime("%d-%m-%Y-%H-%M-%S")
    
    filename = json_filename + "-" + date_time_str + ".json"
    return dirpath + filename


def start_loop(config):
    filepath = load_filepath(config)
    # load an account with the private key
    dev = accounts.add(os.getenv(config['wallets']['from_key'])) 

    # load token infos
    token_name = config["token-info"]["name"]
    token_symbol = config["token-info"]["symbol"]
    token_decimal = config["token-info"]["decimals"]
    token_supply = config["token-info"]["supply"]
    
    # load numbers
    min_random_seconds = config['numbers']['min_random_seconds']
    max_random_seconds = config['numbers']['max_random_seconds']
    max_deploy_number = config['numbers']['max_deploy_number']

    # start loop
    
    latest_timestamp_update = time.time()
    current_timestamp = latest_timestamp_update
    next_random_seconds = random.randint(min_random_seconds, max_random_seconds)
    current_contract_deploy = 0
    token_addresses = []
    
    while current_contract_deploy < max_deploy_number:
        delta_timestamp = current_timestamp - latest_timestamp_update 

        if delta_timestamp >= next_random_seconds:
            token = Token.deploy(token_name, token_symbol, token_decimal, token_supply, {'from': dev}, publish_source=True)
            print('Token address :', token.address)
            token_addresses.append(token.address)
            write_in_file(filepath, token_addresses)

            
            latest_timestamp_update = time.time()
            next_random_seconds = random.randint(min_random_seconds, max_random_seconds)
            print("Next contract in: ", next_random_seconds, " seconds")
            current_contract_deploy += 1

        time.sleep(1)
        current_timestamp = time.time()
    


def main():
    

    # start loop
    start_loop(config)
    print("All contracts have been deployed.")
       
