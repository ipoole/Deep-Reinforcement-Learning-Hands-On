import os
from glob import glob

print(os.getcwd())
files = glob('Chapter??/??_*.py')
for f in files:
    (dir, name) = os.path.split(f)
    newname = 'P'+name
    newfile = os.path.join(dir, newname)
    print("Renaming %s -> %s" % (f, newfile))
    os.rename(f, newfile)

