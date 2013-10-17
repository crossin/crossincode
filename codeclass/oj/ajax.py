from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register

from runcode import run
from models import Quiz


@dajaxice_register
def run_code(request, code, quiz=None):
    if quiz:
        test_code = Quiz.objects.get(id=quiz).test_code
    else:
        test_code = ''
    result = run(code, test_code)
    dajax = Dajax()
    dajax.add_data(result, 'show_result')
    return dajax.json()
