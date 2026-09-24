def language_agent(message):
    """
    Identifies the language of the user's message.
    """

    if any(char in message for char in "ಅಆಇಈಉಊಎಏಐಒಓಕಖಗಘಚಜಟಡತದನಪಬಮಯರಲವಶಸಹ"):
        return "Kannada"

    if any(char in message for char in "अआइईउऊएऐओऔकखगघचछजझटडतदनपबमयरलवशसह"):
        return "Hindi"

    return "English"