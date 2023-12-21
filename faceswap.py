import cv2
import numpy as np
import insightface
from insightface.app import FaceAnalysis
from insightface.data import get_image as ins_get_image

import matplotlib.pyplot as plt 

app = FaceAnalysis(name='buffalo_l')
app.prepare(ctx_id=0, det_size=(640,640))

swapper = insightface.model_zoo.get_model('inswapper_128.onnx', dowload=False, download_zip=False)

arso = cv2.imread('capturedImages\CapturedImage.png')
#plt.imshow(arso[:,:,::-1])
poster = cv2.imread('posters\Acrimony (2018).png')
#plt.imshow(poster[:,:,::-1])
res = poster.copy()

faces = app.get(poster)

arso_faces = app.get(arso)
arso_face = arso_faces[0]

for face in faces:
    res = swapper.get(res, face, arso_face, paste_back=True)

fig, ax = plt.subplots()
ax.imshow(res[:,:,::-1])
ax.axis('off')
plt.savefig('./img/result.png', bbox_inches='tight', pad_inches=0)
