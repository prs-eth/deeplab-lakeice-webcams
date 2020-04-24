import os.path as osp

import numpy as np
import PIL.Image


def lblsave(filename, lbl):
    
    if osp.splitext(filename)[1] != '.png':
        filename += '.png'
    # Assume label ranses [-1, 254] for int32,
    # and [0, 255] for uint8 as VOC.
    if lbl.min() >= -1 and lbl.max() < 255:
        lbl_pil = PIL.Image.fromarray(lbl.astype(np.uint8), mode='P')
        colormap = np.zeros((256, 3), dtype=float)
        colormap[0] = [0, 0, 0]
        colormap[1] = [255, 0, 0]
        colormap[2] = [191, 191, 191]
        colormap[3] = [255, 255, 255]
        colormap[4] = [64, 64, 64]

        lbl_pil.putpalette((colormap * 255).astype(np.uint8).flatten())
        lbl_pil.save(filename)
    else:
        raise ValueError(
            '[%s] Cannot save the pixel-wise class label as PNG. '
            'Please consider using the .npy format.' % filename
        )
