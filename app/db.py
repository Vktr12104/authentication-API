api_keys = {
    "e54d4431-5dab-474e-b71a-0db1fcb9e659": "7oDYjo3d9r58EJKYi5x4E8",
    "5f0c7127-3be9-4488-b801-c7b6415b45e9": "mUP7PpTHmFAkxcQLWKMY8t"
}

users = {
    "7oDYjo3d9r58EJKYi5x4E8": {
        "nama": "Viktor Arsindiantoro--18222083"
    },
    "mUP7PpTHmFAkxcQLWKMY8t": {
        "name": "Alice"
    }
}

def check_api_key(api_key: str):
    return api_key in api_keys

def get_user_from_api_key(api_key: str):
    if api_key not in api_keys:
        raise ValueError("API Key not valid")
    
    user_id = api_keys[api_key]
    return users.get(user_id, None)