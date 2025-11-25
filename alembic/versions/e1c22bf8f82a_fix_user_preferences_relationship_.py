"""Fix user preferences relationship ambiguity

Revision ID: e1c22bf8f82a
Revises: 77e8f8781efa
Create Date: 2025-11-24 13:12:48.592244

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e1c22bf8f82a'
down_revision: Union[str, Sequence[str], None] = '77e8f8781efa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
