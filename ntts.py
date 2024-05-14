import sys
import traceback
import importlib.util
import site

def excepthook_decorator(excepthook):
    def wrapper(*args, **kwargs):
        exctype, value, exctracback = args
        # print(exctype, value, exctracback)
        # package_path = importlib.util.find_spec('numpy').origin
        package_path = site.getsitepackages()[1].replace('\\', '/')
        if exctype == KeyboardInterrupt:
            format = traceback.format_tb(exctracback)
            frame = {'filename': str(package_path)+'/mindx/model.py', 'lineno':23, 'name': format[-1].split('\n')[0].split(' ')[-1], 'line': 'Model.inference(img)', 'locals': None, 'exname': 'KeyboardInterrupt'}
            msg = ''.join(reformat(frame, format))
            print(msg)
        else:
            excepthook(exctype, value, exctracback)
    return wrapper

def reformat(frame, format):
    result = []
    count = 0
    count += 1
    format[0] = 'Traceback (most recent call last):\n' + format[0]
    row = []
    row.append('  File "{}", line {}, in {}\n'.format(
        frame['filename'], frame['lineno'], frame['name']))
    if frame['line']:
        row.append('    {}\n'.format(frame['line'].strip()))
    if frame['locals']:
        for name, value in sorted(frame['locals'].items()):
            row.append('    {name} = {value}\n'.format(name=name, value=value))
    if frame['exname']:
        row.append(frame['exname'])
    result = ''.join(row)
    format[-1] = result
    return format