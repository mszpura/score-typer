""" users table

Revision ID: 106b1e2f6f8f
Revises: 91315f2681b7
Create Date: 2022-01-29 19:23:47.759292

"""
from sqlalchemy.dialects.postgresql import UUID
from alembic import op
from sqlalchemy import Column, Integer, DateTime, JSON, func

# revision identifiers, used by Alembic.
revision = '106b1e2f6f8f'
down_revision = '91315f2681b7'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        Column("table_id", Integer, primary_key=True, autoincrement=True),
        Column("id", UUID(as_uuid=True), unique=True, index=False),
        Column("json", JSON, nullable=False),
        Column("created_date", DateTime, server_default=func.current_timestamp(), nullable=False)
    )


def downgrade():
    op.drop_table("users")
