import datetime

from sqlalchemy import text
from sqlalchemy.orm import mapped_column
from typing import Annotated


# Custom DB types
intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[
    datetime.datetime,
    mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=datetime.datetime.utcnow()
    )
]
str50 = Annotated[str, 50]
