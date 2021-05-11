"""remove coulmn

Revision ID: 239659cf00e8
Revises: 0aed3bd08d28
Create Date: 2021-05-11 10:38:38.986782

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '239659cf00e8'
down_revision = '0aed3bd08d28'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(batch_op.f('fk_answer_submitter_id_submitter'), 'submitter', ['submitter_id'], ['id'])
        batch_op.drop_column('user_id')
        batch_op.drop_column('email_input')
        batch_op.drop_column('name_input')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('username')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.VARCHAR(length=64), nullable=True))

    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name_input', sa.VARCHAR(length=20), nullable=True))
        batch_op.add_column(sa.Column('email_input', sa.VARCHAR(length=20), nullable=True))
        batch_op.add_column(sa.Column('user_id', sa.INTEGER(), nullable=True))
        batch_op.drop_constraint(batch_op.f('fk_answer_submitter_id_submitter'), type_='foreignkey')
        batch_op.create_foreign_key(None, 'user', ['user_id'], ['id'])

    # ### end Alembic commands ###
