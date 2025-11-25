"""Final fix: resolve User-Preferences property scope

Revision ID: 77e8f8781efa
Revises: ef0248477642
Create Date: 2025-11-24 13:03:48.787277

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '77e8f8781efa'
down_revision: Union[str, Sequence[str], None] = 'ef0248477642'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
