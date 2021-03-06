"""This module contains #miraheze-specific commands."""

from __future__ import (
    unicode_literals,
    absolute_import,
    print_function,
    division
)

from sopel.module import commands, example

MIRAHEZE_ABOUT_MIRAHEZE_CHANNEL = (
    'Miraheze is a non-profit wikifarm running MediaWiki. If you would like '
    'more information please see '
    'https://meta.miraheze.org/ or ask in this channel.'
)
MIRAHEZE_ABOUT_OTHER_CHANNELS = (
    'Miraheze is a non-profit wikifarm running MediaWiki. If you would like '
    'more information please see '
    'https://meta.miraheze.org/ or #miraheze.'
)


@commands('miraheze')
@example('.miraheze')
def miraheze(bot, trigger):
    """
    Miraheze about command.

    This command will tell you about Miraheze and where to learn more.
    """
    if trigger.sender == '#miraheze':
        bot.reply(MIRAHEZE_ABOUT_MIRAHEZE_CHANNEL)
    else:
        bot.reply(MIRAHEZE_ABOUT_OTHER_CHANNELS)


@commands('gethelp')
@example('.gethelp I cannot access https://meta.miraheze.org')
def miraheze_gethelp(bot, trigger):
    """Reply to help requests."""
    if trigger.sender == '#miraheze':
        bot.say(trigger.nick + ', needs help. Pinging Reception123, Zppix, '
                'PuppyKun, Voidwalker.')
