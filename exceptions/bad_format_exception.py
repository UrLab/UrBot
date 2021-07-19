class BadFormatException(Exception):
    """Is raise when a command does not follow the regex in src.parser.parse_command"""

    def __init__(self, msg=""):
        super().__init__()
        self.msg = msg

    def __repr__(self):
        return f"BadFormatException : {self.msg}"
