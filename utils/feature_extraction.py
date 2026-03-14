import re
from urllib.parse import urlparse

def extract_url_features(url):
    """
    Extracts 5 key numerical features from a URL for ML classification.
    """
    # 1. Length of the URL
    url_length = len(url)
    
    # 2. Presence of an IP address (e.g., http://192.168.1.1)
    has_ip = 1 if re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', url) else 0
    
    # 3. Presence of the '@' symbol 
    has_at_symbol = 1 if '@' in url else 0
    
    # 4. Number of dots (subdomain chaining)
    dot_count = url.count('.')
    
    # 5. Presence of hyphens in the domain
    try:
        domain = urlparse(url).netloc
        if not domain:
            domain = url
        has_hyphen_domain = 1 if '-' in domain else 0
    except Exception:
        has_hyphen_domain = 0
        
    # Return as a 2D array because Scikit-Learn models expect a list of lists
    return [[url_length, has_ip, has_at_symbol, dot_count, has_hyphen_domain]]