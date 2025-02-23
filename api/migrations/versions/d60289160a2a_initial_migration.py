"""initial migration

Revision ID: d60289160a2a
Revises: 
Create Date: 2025-02-23 00:14:44.210730

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd60289160a2a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('kyc_status', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('last_login', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('category', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('current_stage', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('role', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('extra_details', sa.JSON(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('extra_details')
        batch_op.drop_column('role')
        batch_op.drop_column('current_stage')
        batch_op.drop_column('category')
        batch_op.drop_column('last_login')
        batch_op.drop_column('kyc_status')

    # ### end Alembic commands ###
