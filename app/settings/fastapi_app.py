from fastapi import FastAPI


def create_app():
    app = FastAPI(
        title="Biblioteca API",
        version="1.0.0",
        description="API para gestão básica de livros usando SQLite + SQLAlchemy (assincrono)"
    )

    return app