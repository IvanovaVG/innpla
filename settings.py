from envparse import Env

env = Env()

DATABASE_USER = env.str('POSTGRES_USER', default='postgres')
DATABASE_PASSWORD = env.str('POSTGRES_PASSWORD', default='postgres')
DATABASE = env.str('POSTGRES_DB', default='postgres')
DATABASE_ADDRESS = env.str('POSTGRES_ADDRESS', default='0.0.0.0')
DATABASE_PORT = env.str('POSTGRES_PORT', default='5432')
DATABASE_URL = f'postgresql+asyncpg://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_ADDRESS}:{DATABASE_PORT}/{DATABASE}'
