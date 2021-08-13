"""empty message

Revision ID: 98cb485f1427
Revises: 15b10ad3cee8
Create Date: 2021-08-13 15:26:40.082927

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98cb485f1427'
down_revision = '15b10ad3cee8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tar2bids', schema=None) as batch_op:
        batch_op.add_column(sa.Column('heuristic', sa.String(length=200), nullable=True))
        batch_op.create_index(batch_op.f('ix_tar2bids_heuristic'), ['heuristic'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tar2bids', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_tar2bids_heuristic'))
        batch_op.drop_column('heuristic')

    # ### end Alembic commands ###
