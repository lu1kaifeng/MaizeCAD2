import re

import pyreadr
from pyfaidx import Fasta

if __name__ == '__main__':
    ref = Fasta(r'ref/Zea_mays.AGPv2.dna.toplevel.fa')
    ref
    def read_robj(fp):
        robj, rp = pyreadr.read_r(fp), fp
        objs = pyreadr.list_objects(rp)[0]['object_name']
        robj = robj[objs]
        return robj

    bian_map = read_robj(r'Bian/Map.RData')

    def marker_read():
        map_filtered = bian_map
        map_filtered = {y['number']:y for y in map(lambda x:x.to_dict(),map_filtered.iloc )}
        return map_filtered
        pass

    def hapmap_read():
         return [ read_robj(r'Bian/Parents26_chr'+str(num)+'.RData') for num in range(1,11)]

    hapmap_list = hapmap_read()

    marker_map = marker_read()

    def marker_coverage(name_marker):
        prev_marker = int(name_marker[1:]) - 1
        frm = 1
        if not prev_marker == 0:
            if  marker_map['m'+str(prev_marker)]['chr'] ==marker_map[name_marker]['chr']:
                frm  = int(marker_map['m'+str(prev_marker)]['agp_pos'])
        to = int(marker_map[name_marker]['agp_pos'])
        return marker_map[name_marker]['chr'],frm,to

    marker_coverage('m17')

    def readNAMPHT():
        fp = r'Bian/NAMPHT.RData'
        robj = read_robj(fp)
        for row in robj.itertuples(index=False):
            row_dict = row._asdict()
            marker_values = {k:v for k,v in row_dict.items() if re.match('m.*',k)}
            zygosity = {marker_coverage(k):v for k,v in marker_values.items()}


    def

    readNAMPHT()