"""init

Revision ID: ad5c33ab13e8
Revises: 
Create Date: 2023-12-23 22:28:03.225047

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision: str = 'ad5c33ab13e8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("works",
                    sa.Column("id", sa.Integer, autoincrement=True, nullable=False),
                    sa.Column("work", sa.String(length=30), nullable=False),
                    sa.Column("image_url", sa.String(length=255), nullable=True),
                    sa.Column("created_at", sa.DateTime, nullable=False, server_default=func.now()),
                    sa.Column("updated_at", sa.DateTime, nullable=True),
                    sa.Column("delted_at", sa.DateTime, nullable=True),
                    sa.PrimaryKeyConstraint("id")
                    )
    op.create_table("photos",
                    sa.Column("id", sa.Integer, autoincrement=True, nullable=False),
                    sa.Column("image_url", sa.String(length=255), nullable=True),
                    sa.Column("work_id", sa.Integer, nullable=False),
                    sa.Column("created_at", sa.DateTime, nullable=False, server_default=func.now()),
                    sa.Column("updated_at", sa.DateTime, nullable=True),
                    sa.Column("delted_at", sa.DateTime, nullable=True),
                    sa.PrimaryKeyConstraint("id")
                    )
    op.create_table("menus",
                    sa.Column("id", sa.Integer, autoincrement=True, nullable=False),
                    sa.Column("menu_name", sa.String(length=30), nullable=False),
                    sa.Column("url_path", sa.String(length=30), nullable=False),
                    sa.PrimaryKeyConstraint("id")
                    )
    op.create_foreign_key('photo_work_fk',
                          source_table="photos",
                          referent_table="works",
                          local_cols=['work_id'],
                          remote_cols=['id'],
                          ondelete="CASCADE"
                        )


def downgrade() -> None:
    pass
