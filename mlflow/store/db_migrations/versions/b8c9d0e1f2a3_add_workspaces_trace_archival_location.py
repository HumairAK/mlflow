"""add trace archival workspace columns

Revision ID: b8c9d0e1f2a3
Revises: c3d6457b6d8a
Create Date: 2026-03-30 00:00:00.000000

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "b8c9d0e1f2a3"
down_revision = "c3d6457b6d8a"
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table("workspaces", schema=None) as batch_op:
        batch_op.add_column(sa.Column("trace_archival_location", sa.Text(), nullable=True))
        batch_op.add_column(sa.Column("trace_archival_retention", sa.Text(), nullable=True))


def downgrade():
    with op.batch_alter_table("workspaces", schema=None) as batch_op:
        batch_op.drop_column("trace_archival_retention")
        batch_op.drop_column("trace_archival_location")
