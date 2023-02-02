import random
from typing import Union
from uuid import UUID


async def generate_code_for_activation() -> int:
    return random.randint(100000, 999999)

