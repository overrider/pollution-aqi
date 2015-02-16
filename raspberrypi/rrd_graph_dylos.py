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

import rrdtool
import os

directory = "/controlpanel/public/img/"

if os.path.isdir(directory) == False:
	exit(1)

if os.path.exists("/var/rrd/dylos.rrd") == False:
	exit(1)

for sched in ['hourly','daily','weekly','monthly']:
	if   sched == 'hourly':
	        period = 'h'
	elif sched == 'weekly':
		period = 'w'
	elif sched == 'daily':
		period = 'd'
	elif sched == 'monthly':
		period = 'm'

	ret = rrdtool.graph( "/controlpanel/public/img/metrics-05-%s.png" %(sched), "--start", "-1%s" %(period), "--vertical-label=Particles / 100",
	        '--full-size-mode',
		"--slope-mode",
		"-w 550px",
		"-h 200px",
		"-t Particles <=0.5 micron," + sched,
		"DEF:m1_num=/var/rrd/dylos.rrd:small:AVERAGE",
		"LINE2:m1_num#2AABD2:small\\r")

	ret = rrdtool.graph( "/controlpanel/public/img/metrics-25-%s.png" %(sched), "--start", "-1%s" %(period), "--vertical-label=Particles / 100",
	        '--full-size-mode',
		"--slope-mode",
		"-w 550px",
		"-h 200px",
		"-t Particles >=2.5 micron," + sched,
		"DEF:m1_num=/var/rrd/dylos.rrd:large:AVERAGE",
		"LINE2:m1_num#2AABD2:large\\r")
