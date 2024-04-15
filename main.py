import logging
import sys

from msg.one import one_msg
from msg.two import two_msg

FMT = "%(name)s %(asctime)s %(levelname)s %(message)s"
logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout,
    format=FMT,
    datefmt="%Y-%m-%d %H:%M:%S",
)

log = logging.getLogger(__name__)


def main():
    log.info("Just starting up")
    log.info(one_msg())
    log.info(two_msg())
    log.info("Here is an extra one!")


if __name__ == "__main__":
    main()
