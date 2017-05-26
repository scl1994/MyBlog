"""add confirm

Revision ID: 23689c2e13a7
Revises: f569cc3d127f
Create Date: 2017-05-26 12:33:34.034578

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23689c2e13a7'
down_revision = 'f569cc3d127f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    # ### end Alembic commands ###