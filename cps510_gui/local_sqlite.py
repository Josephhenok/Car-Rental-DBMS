from .settings import *
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
    "oracle": {
        "ENGINE": "django.db.backends.oracle",
        "NAME": os.getenv("ORACLE_DSN", "oracle.scs.ryerson.ca:1521/orcl"),
        "USER": os.getenv("ORACLE_USER", ""),
        "PASSWORD": os.getenv("ORACLE_PASSWORD", ""),
    },
}
