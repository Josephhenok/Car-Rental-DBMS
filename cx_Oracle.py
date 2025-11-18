import os,oracledb
lib=os.getenv("OCI_LIB_DIR")
if lib:
    try: oracledb.init_oracle_client(lib_dir=lib)
    except Exception: pass
from oracledb import *
