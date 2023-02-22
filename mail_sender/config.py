from fastapi_mail import ConnectionConfig

conf = ConnectionConfig(
    MAIL_USERNAME="email@yandex.com",
    MAIL_PASSWORD="password",
    MAIL_FROM='email@yandex.com',
    MAIL_PORT=587,
    MAIL_SERVER="smtp.yandex.ru",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
   # USE_CREDENTIALS=True
)
