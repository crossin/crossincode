#import sys
#from StringIO import StringIO
from RestrictedPython import compile_restricted
#from RestrictedPython.PrintCollector import PrintCollector
from RestrictedPython.Guards import safe_builtins, full_write_guard

from limiter import timelimit


def safe_import(name, *args, **kwargs):
    safe_module = ['math', 'random']
    if name in safe_module:
        return __import__(name, *args, **kwargs)
    else:
        raise RuntimeError('module %s is not allowed to import' % name)


def safe_input(prompt=''):
    SafePrintCollector().write(prompt)
    return ''


class SafePrintCollector:
    txt = []

    def write(self, text):
        SafePrintCollector.txt.append(text)

    def __call__(self):
        return ''.join(SafePrintCollector.txt)

    @classmethod
    def blank(cls):
        cls.txt = []
        return cls


def exec_code(code, _globals):
    exec code in _globals


def run(code):
#    buffer = StringIO()
#    sys.stdin = buffer
#    sys.stdout = buffer
    try:
        safe_builtins['_print_'] = SafePrintCollector.blank()
        safe_builtins['__import__'] = safe_import
        safe_builtins['__name__'] = '__safe_bulitin__'
        safe_builtins['_getattr_'] = getattr
        safe_builtins['_getiter_'] = list
        safe_builtins['_write_'] = full_write_guard
        safe_builtins['input'] = safe_input

        restricted_globals = dict(__builtins__=safe_builtins)
        code += '\nresult = printed'
        code = compile_restricted(code, '<string>', 'exec')
        result = timelimit(0.5, exec_code, kwargs={
            'code': code,
            '_globals': restricted_globals
        }) or restricted_globals['result']
    except Exception, e:
        result = '[Error] %s: %s' % (type(e).__name__, e)
    return result
#    sys.stdin = sys.__stdin__
#    sys.stdout = sys.__stdout__
#    return buffer.getvalue()
