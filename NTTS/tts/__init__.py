import os
import sys

from ..ntts import excepthook_decorator

sys.excepthook = excepthook_decorator(
    sys.excepthook,
    '/root/anaconda3/lib/python3.9/site-packages/mindx/__init__.py',
    57,
    'time.sleep(6)'
)