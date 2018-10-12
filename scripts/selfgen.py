import os
import sys

sys.path.append(os.getcwd())

from codegen.codegen import generate
from codegen.load_config import load_config

generate(load_config(1))
