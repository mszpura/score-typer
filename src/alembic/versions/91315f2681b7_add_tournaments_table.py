"""add tournaments table

Revision ID: 91315f2681b7
Revises: 
Create Date: 2022-01-29 18:18:09.474801

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func

# revision identifiers, used by Alembic.
revision = '91315f2681b7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "tournaments",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("json", sa.JSON, nullable=False),
        sa.Column("created_date", sa.DateTime, default=func.now(), nullable=False)
    )


def downgrade():
    op.drop_table("tournaments")
