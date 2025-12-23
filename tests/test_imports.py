from app.models.item import Item


def test_import_item_model() -> None:
    """
    Test très simple pour vérifier que le modèle Item peut être importé.
    Cela permet à pytest de collecter au moins un test
    et à coverage de mesurer du code dans le package `app`.
    """
    # On utilise Item pour satisfaire Ruff (F401)
    assert Item is not None
