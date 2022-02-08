"""add tournaments table

Revision ID: 91315f2681b7
Revises: 
Create Date: 2022-01-29 18:18:09.474801

"""
from alembic import op
from sqlalchemy import Column, Integer, DateTime, JSON, func
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = '91315f2681b7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "tournaments",
        Column("table_id", Integer, primary_key=True, autoincrement=True),
        Column("id", UUID(as_uuid=True), unique=True, index=True),
        Column("json", JSON, nullable=False),
        Column("created_date", DateTime, server_default=func.current_timestamp(), nullable=False),
        Column("finished_date", DateTime, nullable=True)
    )


def downgrade():
    op.drop_table("tournaments")
