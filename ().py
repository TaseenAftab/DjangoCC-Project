# coding: utf-8
from core.testapp.models import Ifta
Ifta.create_object('AskImam','hanafi')
Ifta.objects.create('AskImam','hanafi')
Ifta.objects.create(name='AskImam',fiqh = 'hanafi')
get_ipython().run_line_magic('save', '()')
Ifta.objects.all()
Ifta.objects.create(name='MalikiMadhabQA',fiqh = 'maliki')
