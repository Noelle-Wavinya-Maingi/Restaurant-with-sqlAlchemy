"""Create the database

Revision ID: 9e11ea3804c8
Revises: 73d55bb2699d
Create Date: 2023-09-03 23:46:23.883852

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e11ea3804c8'
down_revision = '73d55bb2699d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'customer',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('first_name', sa.String(), nullable=True),
        sa.Column('last_name', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        'restaurant',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('price', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        'review',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('star_rating', sa.Integer(), nullable=True),
        sa.Column('customer_id', sa.Integer(), nullable=True),
        sa.Column('restaurant_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['customer_id'], ['customer.id'],),
        sa.ForeignKeyConstraint(['restaurant_id'], ['restaurant.id'],),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade() -> None:
    op.drop_table('review')
    op.drop_table('restaurant')
    op.drop_table('customer')
