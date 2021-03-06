"""initdb

Revision ID: 1cbd633c7843
Revises: d9da56b73b13
Create Date: 2019-05-15 15:24:00.547403

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1cbd633c7843'
down_revision = 'd9da56b73b13'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Jmission',
    sa.Column('g_id', sa.BigInteger(), nullable=False),
    sa.Column('topic', sa.String(length=128), nullable=True),
    sa.Column('desc', sa.String(length=128), nullable=True),
    sa.Column('state', sa.String(length=32), nullable=True),
    sa.Column('checktime', sa.DateTime(), nullable=True),
    sa.Column('endtime', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('g_id')
    )
    op.create_table('Pmission',
    sa.Column('p_id', sa.BigInteger(), nullable=False),
    sa.Column('topic', sa.String(length=128), nullable=True),
    sa.Column('desc', sa.String(length=128), nullable=True),
    sa.Column('exc', sa.String(length=32), nullable=True),
    sa.Column('state', sa.String(length=32), nullable=True),
    sa.Column('checktime', sa.DateTime(), nullable=True),
    sa.Column('endtime', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('p_id')
    )
    op.create_table('company',
    sa.Column('c_id', sa.String(length=32), nullable=False),
    sa.Column('c_name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('c_id')
    )
    op.create_table('job',
    sa.Column('j_id', sa.String(length=32), nullable=False),
    sa.Column('job_name', sa.String(length=64), nullable=True),
    sa.Column('level', sa.String(length=32), nullable=True),
    sa.Column('s_id', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('j_id')
    )
    op.create_table('person',
    sa.Column('uid', sa.String(length=128), nullable=False),
    sa.Column('username', sa.String(length=32), nullable=True),
    sa.Column('permission', sa.String(length=32), nullable=True),
    sa.Column('tel_num', sa.String(length=16), nullable=True),
    sa.Column('password', sa.String(length=16), nullable=True),
    sa.Column('c_id', sa.String(length=32), nullable=True),
    sa.Column('s_id', sa.String(length=32), nullable=True),
    sa.Column('job', sa.BigInteger(), nullable=True),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('section',
    sa.Column('s_id', sa.String(length=32), nullable=False),
    sa.Column('section_name', sa.String(length=64), nullable=True),
    sa.Column('c_id', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('s_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('section')
    op.drop_table('person')
    op.drop_table('job')
    op.drop_table('company')
    op.drop_table('Pmission')
    op.drop_table('Jmission')
    # ### end Alembic commands ###
