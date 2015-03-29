#!/usr/bin/env python

import subprocess
import contextlib
import os

def rebase_dir():
    return 'rebase_demo'

def create_main_branch():
    base_dir = subprocess.check_output('pwd').rstrip()
    full_rebase_dir = base_dir + '/' + rebase_dir()

    if not os.path.exists(full_rebase_dir):
        subprocess.call(['mkdir', full_rebase_dir])

    os.chdir(full_rebase_dir)

    subprocess.call(['git', 'init'])

create_main_branch()
