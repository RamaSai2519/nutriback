import os
from configs.dev_config import DevConfig
from configs.main_config import MainConfig


ENV = os.environ.get('ENV')

if ENV == 'main':
    CONFIG = MainConfig
else:
    CONFIG = DevConfig
    print(f'\n!!! Server started in DEV environment !!!\n')
