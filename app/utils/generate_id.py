import random
import string
import uuid
from datetime import datetime


def generate_id() -> str:
    N = 10
    me: uuid.UUID = uuid.uuid4()
    j: str = str(me)
    k: list[str] = j.split("-")
    res: str = "".join(
                random.choices(string.ascii_lowercase + string.digits, k=N)
            )

    l: str = "".join(k)
    g = datetime.utcnow()
    hh = g.strftime("%Y%m%d%H%M%S")
    m: str = hh + res + l
    return m