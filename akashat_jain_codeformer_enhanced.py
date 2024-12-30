# -*- coding: utf-8 -*-
"""Akashat_jain_Codeformer_enhanced.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fIGbA75ZRIB6LkZDu777ufskIVipxWeJ
"""

# Commented out IPython magic to ensure Python compatibility.
# %cd /content
!rm -rf CodeFormer
!git clone https://github.com/cedro3/CodeFormer.git
# %cd CodeFormer

!pip install -r requirements.txt
!python basicsr/setup.py develop

!python scripts/download_pretrained_models.py facelib
!python scripts/download_pretrained_models.py CodeFormer

from function import *

! mkdir download

video = 'input.mp4' #@param {type:"string"}
video_file = 'movie/'+video
image_dir='inputs/frame/'
image_file='%s.png'

# video_2_images
reset_folder('inputs/frame')
fps, i, interval = video_2_images(video_file, image_dir, image_file)

from google.colab.patches import cv2_imshow
img = cv2.imread('inputs/frame/000000.png')
cv2_imshow(img)

print('fps = ', fps)
print('frames = ', i)
print('interval = ', interval)

from types import FrameType

input_folder = 'inputs/frame'
w = 0.9 #@param {type:"number"}
reset_folder('results/frame_'+str(w))

! python inference_codeformer.py --w $w\
                                  --test_path $input_folder\
                                  --bg_upsampler realesrgan\
                                  --face_upsample

clear_output()

print('makeing movie...')
fps_r = fps/interval
file_path = 'results/frame_'+str(w)+'/final_results/%06d.png'
! ffmpeg -y -r $fps_r -i $file_path -vcodec libx264 -pix_fmt yuv420p -loglevel error out.mp4

print('preparation for sound...')
! ffmpeg -y -i $video_file -loglevel error sound.mp3
! ffmpeg -y -i out.mp4 -i sound.mp3 -loglevel error output.mp4

print('waiting for play movie...')
display_mp4('output.mp4')

from google.colab import files
import shutil
import os


dst_filepath = 'download/'+os.path.splitext(video)[0]+'_s.mp4'
shutil.copy('output.mp4', dst_filepath)
files.download(dst_filepath)

