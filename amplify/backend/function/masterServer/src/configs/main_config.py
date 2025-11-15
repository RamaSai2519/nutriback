from datetime import timedelta


class MainConfig:
    URL = 'https://dmaoafftud.execute-api.us-east-1.amazonaws.com/main/api'
    
    DB_CONFIG = {
        'connection_url': 'mongodb+srv://rama:7MR9oLpef122UCdy@cluster0.fquqway.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0',
    }

    JWT_SECRET_KEY = 'AdminSecret-59737e2029b4aa10f3008f2a5cb372e537ba8d8a4bd05a87efb081d6634df175fec60167bf48cbfe399e5c98d7c8ea27137d44993ab28b71cfe2ae786f5d1952'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)