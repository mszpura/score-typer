""" users table

Revision ID: 106b1e2f6f8f
Revises: 91315f2681b7
Create Date: 2022-01-29 19:23:47.759292

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = '106b1e2f6f8f'
down_revision = '91315f2681b7'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, autoincrement=False),
        sa.Column("json", sa.JSON, nullable=False),
        sa.Column("created_date", sa.DateTime, default=func.now, nullable=False)
    )


def downgrade():
    op.drop_table("users")
