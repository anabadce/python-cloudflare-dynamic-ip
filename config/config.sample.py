import logging

# The Cloudflare zones that contain the records you plan to update, can be 1 or more.
# Your private token with write access to update DNS records in your zone.  
# Example:
# CLOUDFLARE_ZONES = {
#     "b23c8a2207674f7a97e52b73d723c8b0": {
#         "name": "example.com",
#         "token": "xxxxxxxxxxxxxxxxxxxx_xxxxxxxxx"
#     }
# }
CLOUDFLARE_ZONES = {
    "{zone_id}": {
        "name": "{zone_name}",
        "token": "{zone_token}"
    }
}

# The Cloudflare records you plan to update, can be 1 or more across multiple zones.
# Example:
# CLOUDFLARE_RECORDS = [
#     {
#         "zone_id": "b23c8a2207674f7a97e52b73d723c8b0",
#         "name": "home.example.com",
#         "proxied": False
#     }
# ]
CLOUDFLARE_RECORDS = [
    {
        "zone_id": "{zone_id}",
        "name": "{record_name}",
        "proxied": False
    }
]

# Where the log files go
LAST_IP_FILE = "./cloudflare-dynamic-ip-last.txt"
LOG_FILE = "./cloudflare-dynamic-ip.log"

# Log level
LOGGING_LEVEL = logging.INFO

# Where you get the external IP address, this endpoint must return an IP address in plain text
CURRENT_IP_API = "https://api.ipify.org"
