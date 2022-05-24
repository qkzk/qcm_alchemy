"""Reset

Revision ID: d5d7dc6c5cd0
Revises: 57a0f3e9bfae
Create Date: 2022-05-24 06:44:05.489178

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5d7dc6c5cd0'
down_revision = '57a0f3e9bfae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('student', 'name',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('student', 'name',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    # ### end Alembic commands ###
