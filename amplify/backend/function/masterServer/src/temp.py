import json
from models.interfaces import LoginInput
json_obj = {
    "phone": "1234567890",
    "password": "1234567890",
    "address": "123"
}

dataclass_obj = LoginInput(**json_obj)
print(dataclass_obj.phone)

