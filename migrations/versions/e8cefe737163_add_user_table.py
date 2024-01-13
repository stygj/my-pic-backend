"""add user table

Revision ID: e8cefe737163
Revises: ad5c33ab13e8
Create Date: 2024-01-07 00:52:44.877367

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision: str = 'e8cefe737163'
down_revision: Union[str, None] = 'ad5c33ab13e8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("users",
                    sa.Column("id", sa.Integer, autoincrement=True, nullable=False),
                    sa.Column("username", sa.String(length=30), nullable=False),
                    sa.Column("password", sa.String(length=255), nullable=True),
                    sa.Column("created_at", sa.DateTime, nullable=False, server_default=func.now()),
                    sa.Column("updated_at", sa.DateTime, nullable=True),
                    sa.Column("delted_at", sa.DateTime, nullable=True),
                    sa.PrimaryKeyConstraint("id")
                    )


def downgrade() -> None:
    pass
