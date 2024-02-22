"""added updated_at

Revision ID: 2964335013a2
Revises: f0dd44cbb60a
Create Date: 2024-02-20 11:57:52.776947

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2964335013a2'
down_revision = 'f0dd44cbb60a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('productions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('productions', schema=None) as batch_op:
        batch_op.drop_column('updated_at')

    # ### end Alembic commands ###