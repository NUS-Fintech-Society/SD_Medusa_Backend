"""create users table

Revision ID: 28e3464d7b63
Revises: 
Create Date: 2023-06-09 18:06:04.246733

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28e3464d7b63'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String),
        sa.Column("email", sa.String),
        sa.Column("password_hash", sa.String)  # new column for storing hashed passwords
    )


def downgrade():
    op.drop_table("users")
