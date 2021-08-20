"""empty message

Revision ID: cd1bb82fd708
Revises: dbec821937c6
Create Date: 2021-08-12 16:15:20.404423

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd1bb82fd708'
down_revision = 'dbec821937c6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('selected_heuristic', sa.String(length=128), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('selected_heuristic')

    # ### end Alembic commands ###
