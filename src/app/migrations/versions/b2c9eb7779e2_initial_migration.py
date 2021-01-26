from src.app.lib.utils import dbutils

revision = 'b2c9eb7779e2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    statement = """
        CREATE TABLE Users (
        id BIGINT(20) AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(32),
        email VARCHAR(32),
        password VARCHAR(100),
        INDEX(email));
    """
    dbutils.execute_statement(statement)


def downgrade():
    statement = 'DROP TABLE Users;'
    dbutils.execute_statement(statement)
