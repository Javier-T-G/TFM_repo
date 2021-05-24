import os
import glob as gb




# Google Drive folder where the dataset is stored:
data_path = 'gdrive/MyDrive/TFM/TFM/Datasets/oxford'
gap = [1, 2]
reverse = [0, 1]
# Folder with the unzipped rgbd images:
rgbpath = data_path + '/swinging_4_static/rgbd'  # path to the dataset
# Get only the rgb images, and sort them alphanumerically
# "folder" variable contains the path to every image of rgbpath
folder = sorted(gb.glob(os.path.join(rgbpath, '*color.png')))

for r in reverse:
  for g in gap:
    for f in folder:
      print('===> Runing {}, gap {}'.format(f, g))
      mode = 'raft-things.pth'  # model
      if r==1:
        raw_outroot = data_path + '/Flows_gap-{}/'.format(g)  # where to raw flow
        outroot = data_path + '/FlowImages_gap-{}/'.format(g)  # where to save the image flow
      elif r==0:
        raw_outroot = data_path + '/Flows_gap{}/'.format(g)   # where to raw flow
        outroot = data_path + '/FlowImages_gap{}/'.format(g)   # where to save the image flow
      os.system("python predict.py "
                "--gap {} --mode {} --path {} "
                "--outroot {} --reverse {} --raw_outroot {}".format(g, mode, f, outroot, r, raw_outroot))