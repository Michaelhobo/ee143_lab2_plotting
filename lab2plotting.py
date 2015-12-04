import matplotlib.pyplot as plt
from os import walk
from decimal import *
import pdb
fig_num = 1
def graph_from_file(filename, title=None, xlabel="V", ylabel="I"):
  global fig_num
  data = []
  f = open(filename)
  title = filename.replace('.csv', '').replace(dirname, '')
  titlestring = "Setup title"
  for line in f:
    if len(line) > 0:
      if line[0].isdigit() or line[0]=='-':
        data.append([Decimal(s) for s in line.split(',')])
      elif line[0].isalpha():
        data = []
      if not title and titlestring in line:
        linevals = line.split(',')
        if len(line) >= 2:
          title = linevals[1].rstrip().replace('"', '').replace('/','')
  x = []
  y = []
  for d in data:
    x.append(d[0])
    y.append(d[1])
  plt.figure(fig_num)
  fig_num += 1
  plt.plot(x,y)
  if not title:
    title = " "
  plt.title(title)
  plt.xlabel(xlabel)
  plt.ylabel(ylabel)
  outdirname = "plotfiles/"
  plt.savefig(outdirname + title + '.png')
filenames = []
dirname = "datafiles/"
for (dirpath, dirnames, files) in walk(dirname):
  filenames.extend(files)
for filename in filenames:
  graph_from_file(dirname + filename)
print "Entering pdb."
print "Use plt.plot() to show all plots."
pdb.set_trace()
