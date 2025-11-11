#!/usr/bin/env python3
import sys
import time

# Add path for imports
sys.path.append('C:/Users/ksair/Downloads/SRU_071_SIH_25002/tourist-safety-system/backend')

# Wait a moment for server to be ready
time.sleep(2)

# Test using urllib instead of requests
import urllib.request
import json

url = "http://127.0.0.1:5000/api/auth/admin/login"
data = {
    "username": "admin", 
    "password": "admin123"
}

try:
    # Convert data to JSON
    json_data = json.dumps(data).encode('utf-8')
    
    # Create request
    req = urllib.request.Request(url, data=json_data)
    req.add_header('Content-Type', 'application/json')
    
    # Make request
    with urllib.request.urlopen(req) as response:
        result = response.read().decode('utf-8')
        print(f"Status: {response.status}")
        print(f"Response: {result}")
        
except Exception as e:
    print(f"Error: {e}")