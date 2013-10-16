import threading
import inspect
import ctypes


class TimeoutException(Exception):
    pass


def _async_raise(tid, exctype):
    if not inspect.isclass(exctype):
        raise TypeError("Only types can be raised (not instances)")
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(tid),
                                                     ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # "if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, 0)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def timelimit(timeout, func, args=(), kwargs={}):
    class ThreadWithExc(threading.Thread):
        '''A thread class that supports raising exception in the thread from
            another thread.
        '''
        def _get_my_tid(self):
            """determines this (self's) thread id

            CAREFUL : this function is executed in the context of the caller
            thread, to get the identity of the thread represented by this
            instance.
            """
            if not self.isAlive():
                raise threading.ThreadError("the thread is not active")

            # do we have it cached?
            if hasattr(self, "_thread_id"):
                return self._thread_id

            # no, look for it in the _active dict
            for tid, tobj in threading._active.items():
                if tobj is self:
                    self._thread_id = tid
                    return tid
            raise AssertionError("could not determine the thread's id")

        def raiseExc(self, exctype):
            _async_raise(self._get_my_tid(), exctype)

        def __init__(self):
            threading.Thread.__init__(self)
            self.result = None

        def run(self):
            try:
                self.result = func(*args, **kwargs)
            except Exception, e:
                self.result = '[Error] %s: %s' % (type(e).__name__, e)

    it = ThreadWithExc()
    it.start()
    it.join(timeout)
    if it.isAlive():
        it.raiseExc(TimeoutException)
        raise(TimeoutException('The operation has timed out.'))
    else:
        return it.result
