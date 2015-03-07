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

directory = "/controlpanel/public/img/"

if os.path.isdir(directory) == False:
	exit(1)

if os.path.exists("/var/rrd/dylos.rrd") == False:
	exit(1)

ret = rrdtool.graph( "/controlpanel/public/img/metrics-05.png", "--start", "-86400", "--vertical-label=Particles / 100",
        '--full-size-mode',
        "--slope-mode",
        "-w 1050px",
        "-h 300px",
        "-l 0",
        "-t Particles <= 2.5 microns",
        "--grid-dash", "1:0",
        "--font", "TITLE:13:Times",
        '--color', 'BACK#222222',
        '--color', 'CANVAS#222222',
        '--color', 'FONT#FFFFFF',
        '--color', 'AXIS#FEFEFE',
        '--color', 'MGRID#444444',
        '--color', 'GRID#222222',
        '--color', 'SHADEA#000000',
        '--color', 'SHADEB#000000',
        '--color', 'FRAME#EEEEEE',
        '--color', 'ARROW#FEFEFE',
        "--alt-autoscale-max",
        "DEF:savg=/var/rrd/dylos.rrd:small:AVERAGE",
        "AREA:savg#C9FF00:small",
        "GPRINT:savg:LAST:Current\:%8.2lf %s",
        "GPRINT:savg:MIN:Min\:%8.2lf %s",
        "GPRINT:savg:MAX:Max\:%8.2lf %s",
        "GPRINT:savg:AVERAGE:Avg\:%8.2lf %s",
        )

ret = rrdtool.graph( "/controlpanel/public/img/metrics-25.png", "--start", "-86400", "--vertical-label=Particles / 100",
        '--full-size-mode',
        "--slope-mode",
        "-w 1440px",
        "-h 300px",
        "-l 0",
        "-t Particles >= 2.5 microns",
        "--grid-dash", "1:0",
        "--font", "TITLE:13:Times",
        '--color', 'BACK#222222',
        '--color', 'CANVAS#222222',
        '--color', 'FONT#FFFFFF',
        '--color', 'AXIS#FEFEFE',
        '--color', 'MGRID#444444',
        '--color', 'GRID#222222',
        '--color', 'SHADEA#000000',
        '--color', 'SHADEB#000000',
        '--color', 'FRAME#EEEEEE',
        '--color', 'ARROW#FEFEFE',
        "--alt-autoscale-max",
        "DEF:savg=/var/rrd/dylos.rrd:large:AVERAGE",
        "AREA:savg#C9FF00:small",
        "GPRINT:savg:LAST:Current\:%8.2lf %s",
        "GPRINT:savg:MIN:Min\:%8.2lf %s",
        "GPRINT:savg:MAX:Max\:%8.2lf %s",
        "GPRINT:savg:AVERAGE:Avg\:%8.2lf %s",
        )

