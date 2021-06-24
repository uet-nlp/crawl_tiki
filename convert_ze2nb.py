import os, sys

# import zeppelin2nb module
from ze2nb import ze2nb

ze2nb('cuongnm63.json')

# output = os.path.abspath(os.path.join(sys.path[0])) +'/output'
# ze2nb('riiid-madness-training-Catboost.json', out_path=output, to_html=True, to_py=True)