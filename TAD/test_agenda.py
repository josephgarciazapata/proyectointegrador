import pytest

from agenda import Agenda


def test_agregar_incrementa_len():
    agenda = Agenda()
    agenda.agregar("Beto", "3001111111")
    agenda.agregar("Ana", "3002222222")
    assert len(agenda) == 2


def test_contiene_encuentra_nombre_existente():
    agenda = Agenda()
    agenda.agregar("Camila", "3003333333")
    assert agenda.contiene("Camila") is True


def test_contiene_no_encuentra_nombre_ausente():
    agenda = Agenda()
    agenda.agregar("Camila", "3003333333")
    assert agenda.contiene("David") is False


def test_telefono_de_devuelve_el_telefono_correcto():
    agenda = Agenda()
    agenda.agregar("Elena", "3004444444")
    assert agenda.telefono_de("Elena") == "3004444444"


def test_nombres_quedan_en_orden_alfabetico():
    agenda = Agenda()
    for nombre in ["Fabio", "Ana", "David", "Beto"]:
        agenda.agregar(nombre, "0")
    assert agenda.nombres() == ["Ana", "Beto", "David", "Fabio"]


def test_nombres_devuelve_una_copia_independiente():
    agenda = Agenda()
    agenda.agregar("Gustavo", "3005555555")
    copia = agenda.nombres()
    copia.append("Intruso")
    assert agenda.nombres() == ["Gustavo"]


def test_agregar_nombre_repetido_actualiza_telefono_sin_duplicar():
    agenda = Agenda()
    agenda.agregar("Hugo", "3006666666")
    agenda.agregar("Hugo", "3007777777")
    assert len(agenda) == 1
    assert agenda.telefono_de("Hugo") == "3007777777"


def test_eliminar_quita_el_contacto():
    agenda = Agenda()
    agenda.agregar("Irene", "3008888888")
    agenda.agregar("Julio", "3009999999")
    agenda.eliminar("Irene")
    assert len(agenda) == 1
    assert agenda.contiene("Irene") is False
    assert agenda.contiene("Julio") is True


def test_telefono_se_guarda_como_texto():
    agenda = Agenda()
    agenda.agregar("Karla", 3001112233)
    assert agenda.telefono_de("Karla") == "3001112233"
    assert isinstance(agenda.telefono_de("Karla"), str)


def test_borde_agenda_vacia():
    agenda = Agenda()
    assert len(agenda) == 0
    assert agenda.nombres() == []
    assert agenda.contiene("Nadie") is False


def test_borde_nombre_repetido_no_duplica():
    agenda = Agenda()
    agenda.agregar("Laura", "3011111111")
    agenda.agregar("Laura", "3011111111")
    assert len(agenda) == 1


def test_borde_nombre_que_no_esta_lanza_keyerror():
    agenda = Agenda()
    agenda.agregar("Mario", "3012222222")
    with pytest.raises(KeyError):
        agenda.telefono_de("Nombre inexistente")
    with pytest.raises(KeyError):
        agenda.eliminar("Otro nombre inexistente")


def test_borde_nombre_vacio_lanza_valueerror():
    agenda = Agenda()
    with pytest.raises(ValueError):
        agenda.agregar("", "3013333333")


def test_borde_mayusculas_y_tildes_son_nombres_distintos():
    # El operador < de Python compara por código de carácter: las
    # mayúsculas van antes que TODAS las minúsculas. Por eso el orden
    # real es ANA, Ana, ana (no el orden "de diccionario" que uno
    # esperaría a simple vista).
    agenda = Agenda()
    agenda.agregar("ana", "1")
    agenda.agregar("Ana", "2")
    agenda.agregar("ANA", "3")

    assert len(agenda) == 3
    assert agenda.nombres() == ["ANA", "Ana", "ana"]