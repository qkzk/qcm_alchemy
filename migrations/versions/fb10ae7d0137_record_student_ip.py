"""Record student ip

Revision ID: fb10ae7d0137
Revises: dfc6c04713ff
Create Date: 2022-05-24 06:10:42.541074

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb10ae7d0137'
down_revision = 'dfc6c04713ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('student', sa.Column('address', sa.String(length=45), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('student', 'address')
    # ### end Alembic commands ###
