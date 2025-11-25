"""Final fix: remove redundant FK from User model

Revision ID: 17e9155018c3
Revises: 42fce9d7ee35
Create Date: 2025-11-24 12:57:23.567252

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '17e9155018c3'
down_revision: Union[str, Sequence[str], None] = '42fce9d7ee35'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
