import os

import pyreadr

rdata_files = []

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".RData"):
            rdata_files.append(os.path.join(root, file))

for robj,rp in ( (pyreadr.read_r(fp),fp) for fp in rdata_files):
    objs = pyreadr.list_objects(rp)[0]['object_name']
    robj[objs].to_csv(rp+'.csv', index=False)