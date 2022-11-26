from decouple import config


DB_INFO = {"host": config('DB_HOST', default='localhost'),
           "user": config('DB_USER', default='root'),
           "password": config('DB_PASSWORD', default='2404'),
           "dbname": config('DB_NAME', default='contactsdb')}

DATABASE_CONNECTION_URI = f"mysql://{DB_INFO['user']}:{DB_INFO['password']}@{DB_INFO['host']}" \
              f"/{DB_INFO['dbname']}"
