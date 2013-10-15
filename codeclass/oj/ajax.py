from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register

from runcode import run


@dajaxice_register
def run_code(request, code):
    result = run(code)
    dajax = Dajax()
    dajax.assign('#console', 'value', result)
    return dajax.json()
