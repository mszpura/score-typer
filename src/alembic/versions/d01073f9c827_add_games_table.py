"""add_games_table

Revision ID: d01073f9c827
Revises: 106b1e2f6f8f
Create Date: 2022-02-09 16:53:35.557830

"""
from sqlalchemy import Integer, Column, JSON, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from alembic import op


# revision identifiers, used by Alembic.
revision = 'd01073f9c827'
down_revision = '106b1e2f6f8f'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "games",
        Column("table_id", Integer, primary_key=True, autoincrement=True),
        Column("id", UUID(as_uuid=True), unique=True, index=True),
        Column("json", JSON, nullable=False),
        Column("created_date", DateTime, server_default=func.current_timestamp(), nullable=False)
    )


def downgrade():
    pass
