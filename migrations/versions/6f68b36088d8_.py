"""empty message

Revision ID: 6f68b36088d8
Revises: 329b248ddc9b
Create Date: 2020-07-26 22:12:37.722228

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6f68b36088d8'
down_revision = '329b248ddc9b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ihome_house', sa.Column('area', sa.String(length=10), nullable=False))
    op.add_column('ihome_house', sa.Column('city', sa.String(length=10), nullable=False))
    op.add_column('ihome_house', sa.Column('street', sa.String(length=10), nullable=False))
    op.add_column('ihome_house', sa.Column('village', sa.String(length=10), nullable=False))
    op.drop_constraint('ihome_house_ibfk_2', 'ihome_house', type_='foreignkey')
    op.drop_column('ihome_house', 'capacity')
    op.drop_column('ihome_house', 'city_id')
    op.drop_column('ihome_house', 'max_days')
    op.drop_column('ihome_house', 'village_id')
    op.drop_column('ihome_house', 'min_days')
    op.drop_column('ihome_house', 'area_id')
    op.drop_column('ihome_house', 'deposit')
    op.drop_column('ihome_house', 'street_id')
    op.drop_column('ihome_house', 'order_count')
    op.drop_column('ihome_house', 'beds')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ihome_house', sa.Column('beds', mysql.VARCHAR(length=64), nullable=True))
    op.add_column('ihome_house', sa.Column('order_count', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.add_column('ihome_house', sa.Column('street_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.add_column('ihome_house', sa.Column('deposit', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.add_column('ihome_house', sa.Column('area_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.add_column('ihome_house', sa.Column('min_days', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.add_column('ihome_house', sa.Column('village_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.add_column('ihome_house', sa.Column('max_days', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.add_column('ihome_house', sa.Column('city_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.add_column('ihome_house', sa.Column('capacity', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.create_foreign_key('ihome_house_ibfk_2', 'ihome_house', 'ihome_area', ['area_id'], ['id'])
    op.drop_column('ihome_house', 'village')
    op.drop_column('ihome_house', 'street')
    op.drop_column('ihome_house', 'city')
    op.drop_column('ihome_house', 'area')
    # ### end Alembic commands ###
