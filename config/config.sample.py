import logging

CLOUDFLARE_ZONES = {
    "{zone_id}": {
        "id": "{zone_id}",
        "name": "{zone_name}",
        "token": "{zone_token}"
    }
}

CLOUDFLARE_RECORDS = [
    {
        "zone_id": "{zone_id}",
        "name": "{record_name}",
        "proxied": False
    }
]

LAST_IP_FILE = "./cloudflare-dynamic-ip-last.txt"
LOG_FILE = "./cloudflare-dynamic-ip.log"

LOGGING_LEVEL = logging.INFO

CURRENT_IP_API = "https://api.ipify.org"
