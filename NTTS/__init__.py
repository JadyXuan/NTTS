from .ntts import excepthook_decorator, get_package_path
import os
import sys

package_path = get_package_path()
sys.excepthook = excepthook_decorator(sys.excepthook, os.path.join(package_path, 'mindx', 'model.py'), 23, 'Model.inference(img)')