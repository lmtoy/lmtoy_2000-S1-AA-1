#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2000-S1-AA-1"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on['test_seq'] = [ 123456, 123457, -123458, 123459 ]
on['test_rsr'] = [ 134567, 134568, -134569]


#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1['test_seq']   = "extent=120 b_order=1 dv=60 dw=60 pix_list=-15"
pars1['test_rsr']   = "speczoom=97,4 badcb=1/2,3/3"

#        common parameters per source on subsequent runs (run1b, run2b), e.g. bank=0 for WARES
pars2 = {}
pars2['test_seq']   = "bank=0 birdies=512,1024"
pars2['test_rsr']   = ""

#        common parameters per source on subsequent runs (run1c, run2c), e.g. bank=1 for WARES
pars3 = {}
pars3['test_seq']   = "bank=0 pix_list=-13,14,15 birdies=512,1024"
pars2['test_rsr']   = ""

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, pars3, sys.argv)
