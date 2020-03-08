"""
Module with commands used by the bot.
"""
import logging
from typing import List

from django_async.apps.bot.business.command_map import command_now

logger = logging.getLogger(__name__)

COMMAND_TO_ACTION_MAP = {"now": command_now}


async def run_command(cmd: str, cmd_args: List[str], chat_consumer):
    """
    Runs BOT commands if they are found in the command map.
    """
    cmd_function = COMMAND_TO_ACTION_MAP.get(cmd)
    logger.info("Got following cmd_function: %s", cmd_function)

    if cmd_function:
        logger.info("Running command...")
        await cmd_function(chat_consumer, *cmd_args)
