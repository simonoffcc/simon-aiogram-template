"""

Revision ID: 55b3f6f59e23
Revises: 
Create Date: 2023-02-28 15:00:46.270468

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55b3f6f59e23'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'chat',
        sa.Column('chat_id', sa.BigInteger(), nullable=False),
        sa.Column('chat_type', sa.Text(), nullable=False),
        sa.Column('title', sa.Text(), nullable=True),
        sa.Column('chat_name', sa.Text(), nullable=True),
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_chat')),
        sa.UniqueConstraint('chat_id', name=op.f('uq_chat_chat_id')),
    )
    op.create_table(
        'user',
        sa.Column('user_id', sa.BigInteger(), nullable=False),
        sa.Column('user_name', sa.Text(), nullable=True),
        sa.Column('first_name', sa.Text(), nullable=True),
        sa.Column('second_name', sa.Text(), nullable=True),
        sa.Column(
            'language_code', sa.Enum('EN', 'RU', 'UK', name='locales'), nullable=True
        ),
        sa.Column('is_premium', sa.Boolean(), nullable=False),
        sa.Column(
            'role',
            sa.Enum('USER', 'MODERATOR', 'ADMINISTRATOR', name='role'),
            nullable=False,
        ),
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_user')),
        sa.UniqueConstraint('user_id', name=op.f('uq_user_user_id')),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('chat')
    # ### end Alembic commands ###