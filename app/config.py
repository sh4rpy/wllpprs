from dotenv import load_dotenv

import os


load_dotenv()
URL = 'https://api.unsplash.com/photos/random?page=1&query={}&orientation=landscape&client_id={}'
CLIENT_ID = os.getenv('CLIENT_ID')
