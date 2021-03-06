"""records

Revision ID: 790680da6373
Revises: 38d22f26e3af
Create Date: 2018-09-02 15:13:14.955243

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '790680da6373'
down_revision = '38d22f26e3af'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_records_study', table_name='records')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_records_study', 'records', ['study'], unique=False)
    # ### end Alembic commands ###
