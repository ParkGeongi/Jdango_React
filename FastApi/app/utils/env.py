DB_USER = "root"
DB_PASSWORD = "root"
DB_HOST = "172.17.0.1"
#host.docker.internal
DB_NAME = "mydb"
PORT = 3306
CHARSET = "utf8"
DB_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{PORT}/{DB_NAME}"