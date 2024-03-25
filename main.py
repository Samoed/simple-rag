from argparse import ArgumentParser
from logging import config as logging_config
from logging import getLogger

from rag.modules import indexer, router

logger = getLogger(__name__)


def query(q: str):
    """Send a query to the LLM model and return the results."""
    logger.debug("query, q=%s", q)
    router.run(q)


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

    args = ArgumentParser()
    args.add_argument(
        "command",
        nargs=1,
        type=str,
        help="Command to run",
        choices=COMMANDS_TO_METHODS.keys(),
    )
    args.add_argument("query", type=str, nargs="*", help="Query to run")
    args = args.parse_args()

    command: str = args.command[0]
    query: str = " ".join(args.query) if args.query else None

    COMMANDS_TO_METHODS[command](q=query)
