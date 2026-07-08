from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

import os
import sys

# Make sure the app package is in path
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
SRC_ROOT = os.path.join(PROJECT_ROOT, "src")
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
if SRC_ROOT not in sys.path:
    sys.path.insert(0, SRC_ROOT)

try:
    from main import app  # noqa: E402
except Exception:
    # main may not be importable in some environments; ignore if missing
    app = None

config = context.config
if config.config_file_name is not None:
    try:
        fileConfig(config.config_file_name)
    except Exception:
        # some test configs (sqlite_test) may not include logging sections
        pass

# Import the metadata from our models package
try:
    from models import Base  # type: ignore

    target_metadata = Base.metadata
except Exception:
    target_metadata = None

# Allow overriding the sqlalchemy URL with the DATABASE_URL env var
db_url = os.environ.get('DATABASE_URL')
if db_url:
    config.set_main_option('sqlalchemy.url', db_url)


def run_migrations_offline() -> None:
    url = config.get_main_option('sqlalchemy.url')
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True)
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
