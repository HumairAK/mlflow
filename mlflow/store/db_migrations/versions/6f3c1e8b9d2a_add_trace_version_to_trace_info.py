"""add trace version to trace_info

Revision ID: 6f3c1e8b9d2a
Revises: da6fb0208061

Create Date: 2026-04-24 14:45:00.000000

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "6f3c1e8b9d2a"
down_revision = "da6fb0208061"
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table("trace_info", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column("trace_version", sa.BigInteger(), nullable=False, server_default="0")
        )


def downgrade():
    with op.batch_alter_table("trace_info", schema=None) as batch_op:
        batch_op.drop_column("trace_version")
