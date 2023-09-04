"""Renaming students to scholars

Revision ID: 43cb5582e3a7
Revises: 
Create Date: 2023-09-01 17:23:23.380108

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '43cb5582e3a7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
