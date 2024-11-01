from typing import Literal

from sqlalchemy.orm import mapped_column, Mapped

from db import Base


class Participant(Base):
    __tablename__ = 'participant'

    id: Mapped[int] = mapped_column(primary_key=True, auto_increment=True)

    name: Mapped[str]
    surname: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    avatar: Mapped[bytes | None]
    gender: Mapped[Literal["male", "female", "other"]] = mapped_column(server_default="other")
