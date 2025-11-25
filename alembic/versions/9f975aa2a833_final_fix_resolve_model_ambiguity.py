"""Final fix: resolve model ambiguity

Revision ID: 9f975aa2a833
Revises: e1c22bf8f82a
Create Date: 2025-11-24 13:27:09.056982

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9f975aa2a833'
down_revision: Union[str, Sequence[str], None] = 'e1c22bf8f82a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
