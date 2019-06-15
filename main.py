# written by SD
# twitter.com/ciphersuites

from classes.size_raffle import SizeRaffle
import json

try:
    config = json.load(open('config.json'))

    email = config['email']
    city = config['city']
    country = config['country']
    store_location = config['store_location']
    specific_size = config['specific_size']
    entries = config['entries']

    proxies = open('proxies.txt').readlines()
    print("Loaded %d proxies"%len(proxies))

    raffle = SizeRaffle(email, city, country, store_location, specific_size, proxies)
    raffle.run(entries)

# case where config file is missing
except FileNotFoundError:
    print("FATAL ERROR: Could not find config file")

# case where config file is not valid json
except json.decoder.JSONDecodeError:
    print("FATAL ERROR: Could not read config file, invalid JSON")

# case where we don't know the cause of the exception
except Exception as e:
    print("Unknown error: " + str(e))