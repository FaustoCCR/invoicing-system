"""map invoice model fields

Revision ID: 6cbf6fd36b3c
Revises: 1ed4a1d02326
Create Date: 2024-12-27 16:42:29.397036

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6cbf6fd36b3c'
down_revision = '1ed4a1d02326'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.alter_column('unit_price',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=2),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.alter_column('unit_price',
               existing_type=sa.Float(precision=2),
               type_=sa.REAL(),
               existing_nullable=False)

    # ### end Alembic commands ###