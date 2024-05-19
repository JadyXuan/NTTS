from .ntts import excepthook_decorator
import sys

sys.excepthook = excepthook_decorator(sys.excepthook)