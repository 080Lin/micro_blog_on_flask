"""article theme

Revision ID: 72eb7e460957
Revises: 
Create Date: 2021-11-30 16:28:33.989267

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72eb7e460957'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('article', sa.Column('theme', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('article', 'theme')
    # ### end Alembic commands ###
