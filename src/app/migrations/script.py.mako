from src.app.lib.utils import dbutils

revision = ${repr(up_revision)}
down_revision = ${repr(down_revision)}
branch_labels = ${repr(branch_labels)}
depends_on = ${repr(depends_on)}


def upgrade():
    statement = """

    """
    dbutils.execute_statement(statement)


def downgrade():
    statement = """

    """
    dbutils.execute_statement(statement)
