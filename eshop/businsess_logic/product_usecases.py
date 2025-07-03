import uuid
from typing import Optional, List

from eshop.businsess_logic.product import Product
from eshop.data_access.product_repo import save, get_by_id, delete_by_id, get_many


def product_create(product_name, product_price) -> Product:

    product = Product(
        id=str(uuid.uuid4()),
        name=product_name,
        price=product_price,
    )
    save(product)

    return product


def product_get_by_id(id: str) -> Optional[Product]:
    return get_by_id(id)


def product_get_many(page: int, limit: int) -> List[Product]:
    return get_many(page=page, limit=limit)
