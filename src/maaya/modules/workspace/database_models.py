from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, ForeignKey, String, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column

from maaya.core.database_model_base import DatabaseBase


class Workspace(DatabaseBase):
    __tablename__ = "workspaces"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)

    name: Mapped[str] = mapped_column(String(200), nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )


class User(DatabaseBase):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)

    email: Mapped[str] = mapped_column(
        String(320),
        nullable=False,
        unique=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )


class Membership(DatabaseBase):
    __tablename__ = "memberships"
    
    __table_args__ = (
    UniqueConstraint(
        "user_id",
        "workspace_id",
        name="uq_memberships_user_workspace",
    ),
)
   

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)

    user_id: Mapped[UUID] = mapped_column(
     ForeignKey("users.id"),
     nullable=False,
    )

    workspace_id: Mapped[UUID] = mapped_column(
     ForeignKey("workspaces.id"),
     nullable=False,
    )
    role: Mapped[str] = mapped_column(
     String(50),
     nullable=False,
    )
    created_at: Mapped[datetime] = mapped_column(
     DateTime(timezone=True),
     server_default=func.now(),
     nullable=False,
    )