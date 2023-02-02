from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hasher:
    @staticmethod
    def verify_password(got_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(got_password, hashed_password)

    @staticmethod
    def hash_password(got_password: str) -> str:
        return pwd_context.hash(got_password)
