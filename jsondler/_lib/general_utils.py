# Attention: this script can not import code from other parts of bill-rec
import os
import random
import string


def generate_random_string(l=10):
    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(l))
