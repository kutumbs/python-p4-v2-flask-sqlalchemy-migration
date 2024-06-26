"""rename address

Revision ID: 27cb9ed48280
Revises: 9362e830c7c4
Create Date: 2024-04-06 18:39:30.276546

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27cb9ed48280'
down_revision = '9362e830c7c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
   op.alter_column('departments', 'address',  new_column_name='location')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
   op.alter_column('departments', 'location',  new_column_name='address')
    # ### end Alembic commands ###
