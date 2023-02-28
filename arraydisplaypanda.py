from direct.showbase.ShowBase import ShowBase
import cv2
from panda3d.core import CardMaker, Texture, TextureStage, PNMImage
import numpy as np

def new_tex():
    #frame_image = cv2.imread('sample_image.png')
    #frame_image = cv2.cvtColor(frame_image, cv2.COLOR_BGR2RGB) 
    L = 256*4
    frame = np.random.randint(0,255,(L,L,3)).astype(np.uint8)

    buf = np.transpose(frame, axes=[1,0,2]).tobytes() # slice RGB to gray scale, transpose 90 degree, convert to text buffer

    h,w,_ = frame.shape
    tex = Texture()
    tex.setup2dTexture(h,w, Texture.T_unsigned_byte, Texture.F_rgb8)
    tex.setRamImageAs(buf, "RGB")
    return tex

base = ShowBase()

# Load the image as a texture
cm = CardMaker('card')

card = render2d.attachNewNode(cm.generate())
card.setScale(2, 1, 2)
card.setPos(-1, 0, -1)

def updateTex(task):
    tex = new_tex()
    card.setTexture(tex) # now apply it to the card
    return task.cont

def quit_app(): import sys; sys.exit()
base.accept("escape", quit_app)

taskMgr.add(updateTex, 'video frame update')
base.run()

