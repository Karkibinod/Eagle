"""Final fix: remove redundant FK from User model

Revision ID: ef0248477642
Revises: 17e9155018c3
Create Date: 2025-11-24 12:59:38.481876

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ef0248477642'
down_revision: Union[str, Sequence[str], None] = '17e9155018c3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
