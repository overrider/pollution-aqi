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

import time
import os
import sys
import io
from rrdtool import update as rrd_update
import subprocess
from subprocess import call

# 2015-02-15 15:08:27,1423984107,dyson-home,55265eb971242335613c81da8bdbfd54,China,Guangdong,Dongguan,14075,230,0

with open('/dylos.txt','r') as fh:
    for line in fh:
        pass
    last = line
    last = last.rstrip()
    data = last.split(",")
    fh.close()

epoch= int(data[0])
small = int(data[3])
large = int(data[4])

if not os.path.exists("/var/rrd/dylos.rrd"):
    subprocess.call(["/usr/local/bin/rrd_create.py"])

if not os.path.exists("/var/rrd/dylos.rrd"):
    sys.exit(1)

def is_number(s):
    try:
        float(s)
        return s
    except ValueError:
        return 0

small = is_number(small)
large = is_number(large)

ret = rrd_update('/var/rrd/dylos.rrd', str(epoch)+':%s:%s' %(small,large));
sys.exit(0)
