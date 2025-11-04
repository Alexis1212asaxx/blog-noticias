from app.main import app


def test_app_existe():
    assert app is not None


def test_home_ruta():
    cliente = app.test_client()
    respuesta = cliente.get('/')
    assert respuesta.status_code == 200
    assert b"Blog de Noticias" in respuesta.data
