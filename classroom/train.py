import json
from django.test import TestCase
from classroom.models import *

# Create your tests here.
if __name__ == '__main__':
    for c in Student.objects.all():
        print(c.id, c.first_name)          