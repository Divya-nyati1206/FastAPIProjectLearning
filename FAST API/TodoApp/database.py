from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:Divya%401206@127.0.0.1:3306/todoapplicationdatabase'
SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
