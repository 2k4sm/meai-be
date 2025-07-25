"""creates table for UserToolPreferenceStorage

Revision ID: 3845090daa59
Revises: 5cab1373b32e
Create Date: 2025-07-20 02:03:08.996786

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3845090daa59'
down_revision: Union[str, Sequence[str], None] = '5cab1373b32e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_tool_preferences',
    sa.Column('preference_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('toolkit_slug', sa.String(length=100), nullable=False),
    sa.Column('is_enabled', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('preference_id')
    )
    op.create_index(op.f('ix_user_tool_preferences_preference_id'), 'user_tool_preferences', ['preference_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_tool_preferences_preference_id'), table_name='user_tool_preferences')
    op.drop_table('user_tool_preferences')
    # ### end Alembic commands ###
