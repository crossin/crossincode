import sys
from traceback import extract_tb
from StringIO import StringIO


def run(code):
    buffer = StringIO()
    sys.stdin = buffer
    sys.stdout = buffer
    try:
        exec code
    except Exception, e:
        print '[Error] Line %d: <%s> %s' % (
            extract_tb(sys.exc_traceback)[-1][1],
            type(e).__name__,
            e)
    sys.stdin = sys.__stdin__
    sys.stdout = sys.__stdout__
    return buffer.getvalue()
