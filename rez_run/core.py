def get_message_from_run():
    from rez.config import config
    message = config.plugins.command.run.message
    return message
