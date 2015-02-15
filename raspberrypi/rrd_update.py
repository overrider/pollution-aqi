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

with open('/dyson.txt','r') as fh:
    for line in fh:
        pass
    last = line
    last = last.rstrip()
    data = last.split(",")
    fh.close()

epoch= int(time.time())
pm05 = int(data[7])
pm25 = int(data[8])

if not os.path.exists("/var/rrd/pollution05.rrd"):
    subprocess.call(["/usr/local/bin/rrd_create.py"])

if not os.path.exists("/var/rrd/pollution25.rrd"):
    subprocess.call(["/usr/local/bin/rrd_create.py"])

def is_number(s):
    try:
        float(s)
        return s
    except ValueError:
        return 0

pm05 = is_number(pm05)
pm25 = is_number(pm25)

if os.path.exists("/var/rrd/pollution05.rrd"):
    ret = rrd_update('/var/rrd/pollution05.rrd', 'N:%s' %(pm05));
else:
    sys.exit(1)

if os.path.exists("/var/rrd/pollution25.rrd"):
    ret = rrd_update('/var/rrd/pollution25.rrd', 'N:%s' %(pm25));
else:
    sys.exit(1)

sys.exit(0)
