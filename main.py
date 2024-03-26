from argparse import ArgumentParser
from logging import config as logging_config
from logging import getLogger

from rag.db import stop
from rag.modules import indexer, router

logger = getLogger(__name__)


def query(q: str):
    """Send a query to the router."""
    logger.debug("query, q=%s", q)

    result: str = router.run(q)
    print("Result: ", result)


def index(*args, **kwargs):
    """Index data from data folder."""
    logger.debug("index")
    indexer.run()


COMMANDS_TO_METHODS = {"query": query, "index": index}


if __name__ == "__main__":
    logging_config.dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "default": {
                    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                },
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "level": "DEBUG",
                    "formatter": "default",
                },
            },
            "loggers": {
                "": {
                    "handlers": ["console"],
                    "level": "DEBUG",
                },
            },
        }
    )

    arg_parser = ArgumentParser()
    arg_parser.add_argument(
        "command",
        nargs=1,
        type=str,
        help="Command to run",
        choices=COMMANDS_TO_METHODS.keys(),
    )
    arg_parser.add_argument("query", type=str, nargs="*", help="Query to run")
    arg_parser = arg_parser.parse_args()

    command: str = arg_parser.command[0]
    query: str = " ".join(arg_parser.query) if arg_parser.query else None

    try:
        COMMANDS_TO_METHODS[command](q=query)
    finally:
        stop()
