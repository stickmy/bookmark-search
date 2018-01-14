# -*- coding: utf-8 -*-
# @author wuwaki
# @date 2018/1/14

import random
import string


def get_ranstr():
    return ''.join(random.sample(string.ascii_letters + string.digits, 8))
