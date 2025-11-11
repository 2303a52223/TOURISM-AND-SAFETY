#!/usr/bin/env python3
import requests
import json

def test_admin_login_request():
    """Test actual admin login request to the running server"""
    try:
        url = "http://127.0.0.1:5000/api/auth/admin/login"
        
        # Test data
        login_data = {
            "username": "admin",
            "password": "admin123"
        }
        
        print(f"Testing admin login request to: {url}")
        print(f"Login data: {json.dumps(login_data, indent=2)}")
        
        # Make the request
        response = requests.post(
            url, 
            json=login_data,
            headers={'Content-Type': 'application/json'},
            timeout=10
        )
        
        print(f"Response status code: {response.status_code}")
        print(f"Response headers: {dict(response.headers)}")
        
        try:
            response_data = response.json()
            print(f"Response JSON: {json.dumps(response_data, indent=2)}")
        except:
            print(f"Response text: {response.text}")
        
        return response.status_code == 200
        
    except Exception as e:
        print(f"Error testing admin login request: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    test_admin_login_request()