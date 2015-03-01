#!/usr/bin/env python2.7

#	Copyright (c) 2012 by David Schulz (ds@ironwhale.com)
#	All rights reserved.
#
#	THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#	ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#	WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#	DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
#	ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
#	(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#	LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
#	ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#	(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#	SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import sys
import shutil
import os
import time
import rrdtool
import time
import io
from rrdtool import update as rrd_update
import subprocess
from subprocess import call
import rrdtool

def is_number(s):
    try:
        float(s)
        return s
    except ValueError:
        return 0

with open('/dylos_rrd.txt','r') as fh:
    for line in fh:
        line = line.rstrip()

    # Last Line
    data = line.split(",")
    epoch= int(data[0])
    small = int(data[3])
    large = int(data[4])
    small = is_number(small)
    large = is_number(large)

    epoch = int(time.time()) # overwrite so it 'works' for dylos continous and monitor mode
    ret = rrd_update('/var/rrd/dylos.rrd', str(epoch)+':%s:%s' %(small,large));

    fh.close()
