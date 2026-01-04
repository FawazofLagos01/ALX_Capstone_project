import uuid

def generate_wallet_address():
    """Generate a unique wallet address."""
    return str(uuid.uuid4())