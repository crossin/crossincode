from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register


@dajaxice_register
def run_code(request):
    dajax = Dajax()
    result = 'helloword'
    dajax.assign('#console', 'value', result)
    return dajax.json()
