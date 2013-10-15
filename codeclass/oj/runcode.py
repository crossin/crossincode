import sys
from StringIO import StringIO


def run(code):
    buffer = StringIO()
    sys.stdin = buffer
    sys.stdout = buffer
    try:
        exec code
    except Exception, e:
        print '[Error] %s: %s' % (type(e).__name__, e)
    sys.stdin = sys.__stdin__
    sys.stdout = sys.__stdout__
    return buffer.getvalue()
