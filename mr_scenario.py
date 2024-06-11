import trimesh
import ipyvolume as ipv
import numpy as np
import warnings
import time

warnings.filterwarnings('ignore')

# This function plots virtual MR UI elements according to an array of their respective [x,y,z] positions
# e.g., plot_mr_scenario([[]])
def plot(ui_properties, gaze=False):
    """
    Plot the MR scenario specified above.

    Parameters:
        ui_properties (array): position of the UI element and width of the UI element.
        gaze (boolean): Plot gaze line.

    Returns:
        float: Time (T) in seconds to hit the target.
    """
    # Load the model from (https://skfb.ly/n5k4i3fdc0) by onmioji
    # licensed under Creative Commons Attribution (http://creativecommons.org/licenses/by/4.0/).
    mesh = trimesh.load_mesh("model.stl")
    vertices = mesh.vertices
    faces = mesh.faces

    fig = ipv.figure()
    # Plot the 3D model
    vertices = vertices / 300 + [0.5, 1, 0]
    ipv.plot_trisurf(vertices[:, 0], vertices[:, 1], vertices[:, 2], triangles=faces)
    # Plot the UI element
    for ui in ui_properties:
        ipv.plot_trisurf([ui[0]-ui[3]/2, ui[0]+ui[3]/2, ui[0]-ui[3]/2, ui[0]+ui[3]/2],
         [ui[1]-ui[3]/2, ui[1]+ui[3]/2, ui[1]+ui[3]/2, ui[1]-ui[3]/2], ui[2],
            triangles=[[0, 2, 3], [2, 3, 1]], color="blue")

    if gaze:
        x = 0.5
        y = 1.8
        z = np.linspace(0, 1, 100)
        ipv.plot(x, y, z, color='blue', size=2)

    ipv.pylab.xyzlabel("X [m]", "Y [m]", "Z [m]")

    ipv.show()