import requests
import socket
from urllib.parse import urlparse

def get_ip_from_url(url):
    try:
        domain = urlparse(url).netloc
        if not domain:
            domain = url
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except Exception:
        return None

def track_location(ip_address):
    try:
        # Using a free IP geolocation API
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        if response.status_code == 200:
            data = response.json()
            if data['status'] == 'success':
                return {
                    "IP": ip_address,
                    "Country": data.get("country"),
                    "City": data.get("city"),
                    "ISP": data.get("isp"),
                    "Lat": data.get("lat"),
                    "Lon": data.get("lon")
                }
    except Exception:
        return None
    return {"Error": "Could not track location"}