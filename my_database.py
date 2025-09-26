import sqlalchemy as db
from sqlalchemy import URL

## control database

def get_engines():
    connection_string = URL.create(
        "postgresql",
        username="Hamid-adm",
        password="npg_SLzvBeIg1yZ4",
        host="ep-royal-sound-a11bau9c.ap-southeast-1.pg.koyeb.app",
        database="koyebdb",
    )
    engine = db.create_engine(connection_string)
    return engine
