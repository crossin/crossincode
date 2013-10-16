from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register

from runcode import run


@dajaxice_register
def run_code(request, code):
    result = run(code)
    dajax = Dajax()
    dajax.add_data(result, 'show_result')
    return dajax.json()
