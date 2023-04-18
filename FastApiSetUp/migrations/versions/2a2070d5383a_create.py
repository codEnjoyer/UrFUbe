"""create

Revision ID: 2a2070d5383a
Revises: 57d3cf53f2d7
Create Date: 2023-04-18 16:38:59.439549

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a2070d5383a'
down_revision = '57d3cf53f2d7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('id', sa.Integer(), nullable=False))
    op.add_column('user', sa.Column('username', sa.String(), nullable=False))
    op.add_column('user', sa.Column('registered_at', sa.TIMESTAMP(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'registered_at')
    op.drop_column('user', 'username')
    op.drop_column('user', 'id')
    # ### end Alembic commands ###
