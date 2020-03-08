"""
Module with utility functions applied to commands and bots.
"""
import logging
import re
from typing import List
from typing import Optional
from typing import Pattern
from typing import Tuple

logger = logging.getLogger(__name__)


def get_command_from_user_message(chat_message: str) -> Tuple[Optional[str], Optional[List]]:
    """
    Attempts to extract a command from a user message.
    """
    command_pattern = re.compile(r"^/(?P<command>\w+)(?P<args>.*)", re.IGNORECASE)  # type: Pattern[str]
    match_rslt = re.search(command_pattern, chat_message)

    if match_rslt is not None:
        command = match_rslt.group("command")
        command_args = match_rslt.group("args").strip().split(" ")
        logger.info("Got the following command: %s and command_args: %s", command, command_args)

        return command, command_args

    logger.info("No commands found!")
    return None, None
