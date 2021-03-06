import matplotlib.pyplot as plt
from os import walk
from decimal import *
import pdb
from sys import argv
import numpy
fig_num = 1
def graph_from_file(filename, title=None, xlabel="V (V)", ylabel="I (A)"):
  global fig_num
  data = []
  f = open(filename)
  title = filename.replace('.csv', '').replace(dirname, '')
  titlestring = "Setup title"
  for line in f:
    if len(line) > 0:
      if line[0].isdigit() or line[0]=='-':
        try:
          data.append([Decimal(s) for s in line.split(',')[0:2]])
        except:
          pdb.set_trace()
      elif line[0].isalpha():
        data = []
      if not title and titlestring in line:
        linevals = line.split(',')
        if len(line) >= 2:
          title = linevals[1].rstrip().replace('"', '').replace('/','')
  only_zero = False
  if len(argv) is 3:
    mu = int(argv[2])
    x = numpy.linspace(0,5,100)
    Cox = 1.86249*10**(-8)
    Vt = float(argv[1])
    shift_y = 0.00000025
    y = mu*Cox/2*(x-Vt)**2+shift_y
    plt.plot(x,y)
    title = "VT = " + argv[1] + "; mu = " + argv[2]
    only_zero = True
  x = []
  y = []
  xy = []
  last_x = None
  for d in data:
    if (not last_x) or (last_x and last_x <= d[0]):
      x.append(d[0])
      y.append(d[1])
      last_x = d[0]
    else:
      if not only_zero:
        last_x = None
        xy.append(x)
        xy.append(y)
        xy.append('b-')
        x = []
        y = []
  xy.append(x)
  xy.append(y)
  xy.append('b-')
  plt.figure(fig_num)
  fig_num += 1
  plt.plot(*xy)
  if not title:
    title = " "
  plt.title(title)
  if any(dev_id in title for dev_id in ["[3]","[4]","[5]"]):
    xlabel = "BIASVAL (V)"
    ylabel = "CX (F)"
  if "I-VD" in title:
    ylabel = "ID (A)"
    xlabel = "VD (V)"
  if "I-VG" in title:
    ylabel = "ID (A)"
    xlabel = "VG (V)"
  if any(dev_id in title for dev_id in ["[2a]","[2b]"]):
    ylabel = "IS1 (A)"
    xlabel = "VDIF (V)"
  if any(dev_id in title for dev_id in ["[7]","[2c]","[2d]"]):
    ylabel = "IA (A)"
    xlabel = "VA (V)"
  if "[14]" in title:
    xlabel = "VIN (V)"
    ylabel = "VOUT (V)"
  plt.xlabel(xlabel)
  plt.ylabel(ylabel)
  outdirname = "plotfiles/"
  plt.savefig(outdirname + title + '.png',bbox_inches="tight")
filenames = []
dirname = "datafiles/"
for (dirpath, dirnames, files) in walk(dirname):
  filenames.extend(files)
for filename in filenames:
  graph_from_file(dirname + filename)
print "Entering pdb."
print "Use plt.plot() to show all plots."
pdb.set_trace()
