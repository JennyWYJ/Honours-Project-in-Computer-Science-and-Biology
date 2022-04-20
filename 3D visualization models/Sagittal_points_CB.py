# This program serves to display the CN neurons from our dataset into a 3D rendering of a sagittal cerebellar slice in Brainrender.

import random
from tkinter import W

import brainrender as b
import imgkit
import numpy as np
from brainrender.actors import Point

from read_csv import all_cells

regions = ['CB', 'CH'] #Not used
zone1 = ['LING', 'CENT', 'CUL']
zone2 = ['DEC', 'FOTU']
zone3 = ['PYR', 'UVU']
zone4 = ['NOD']

# Rendering settings
b.settings.WHOLE_SCREEN = False
b.settings.SHADER_STYLE = "plastic"
b.settings.ROOT_ALPHA = 0.1

# Color palette for zonal connectivity patterns
zonal_colors = {}
zonal_count = {}

# Sets a number n of random points in a specific region
def set_n_points(region, n):
    region_bounds = region.mesh.bounds()

    # testing with random coordinates
    X = np.random.randint(region_bounds[0], region_bounds[1], size=10000)
    Y = np.random.randint(region_bounds[2], region_bounds[3], size=10000)
    Z = np.random.randint(region_bounds[4], region_bounds[5], size=10000)

    points = [[x,y,z] for x,y,z in zip(X, Y, Z)]

    inside_points = region.mesh.insidePoints(points).points()
    #print(points)
    return np.vstack(random.choices(inside_points, k=n))

# Create a point actor at a specific coordinate with a specific color depending on the connectivity zones.
# Keeps track of the pattern colours and cell count for each pattern.
def create_point(x, y, z, zones): 
    cell_coords = [x, y, z]
    if type(zones) == str:
        if zones == "None":
            new_cell = Point(cell_coords, color="lightgrey", radius=10, alpha=3)
            zonal_colors["None"] = "lightgray"
            if "None" not in zonal_count:
                zonal_count["None"] = 1
            else:
                zonal_count["None"] += 1
            return new_cell
        if zones == "Anterior":
            new_cell = Point(cell_coords, color="#58427c", radius=10, alpha=3)
            zonal_colors["Anterior"] = "#58427c"
            if "Anterior" not in zonal_count:
                zonal_count["Anterior"] = 1
            else:
                zonal_count["Anterior"] += 1
            return new_cell
        elif zones == "Central":
            new_cell = Point(cell_coords, color="#ffb347", radius=10, alpha=2.5)
            zonal_colors["Central"] = "#ffb347"
            if "Central" not in zonal_count:
                zonal_count["Central"] = 1
            else:
                zonal_count["Central"] += 1
            return new_cell
        elif zones == "Posterior":
            new_cell = Point(cell_coords, color="#a32638", radius=10, alpha=2.5)
            zonal_colors["Posterior"] = "#a32638" 
            if "Posterior" not in zonal_count:
                zonal_count["Posterior"] = 1
            else:
                zonal_count["Posterior"] += 1
            return new_cell
        elif zones == "Nodular":
            new_cell = Point(cell_coords, color="#5f9ea0", radius=10, alpha=2.5)
            zonal_colors["Nodular"] = "#5f9ea0"
            if "Nodular" not in zonal_count:
                zonal_count["Nodular"] = 1
            else:
                zonal_count["Nodular"] += 1
            return new_cell
    elif len(zones) == 4:
        new_cell = Point(cell_coords, color="black", radius=10, alpha=2.5)
        zonal_colors["All 4 zones"] = "black"
        if "All 4 zones" not in zonal_count:
                zonal_count["All 4 zones"] = 1
        else:
                zonal_count["All 4 zones"] += 1
        return new_cell
    elif len(zones) == 3:
        if "Anterior" not in zones:
            new_cell = Point(cell_coords, color="#ba55d3", radius=10, alpha=2.5)
            zonal_colors["Central, Posterior, Nodular"] = "#ba55d3"
            if "Central, Posterior, Nodular" not in zonal_count:
                zonal_count["Central, Posterior, Nodular"] = 1
            else:
                zonal_count["Central, Posterior, Nodular"] += 1
            return new_cell
        elif "Central" not in zones: #Not represented in dataset
            new_cell = Point(cell_coords, color="peacock", radius=10, alpha=2.5)
            zonal_colors["Anterior, Posterior, Nodular"] = "peacock"
            if "Anterior, Posterior, Nodular" not in zonal_count:
                zonal_count["Anterior, Posterior, Nodular"] = 1
            else:
                zonal_count["Anterior, Posterior, Nodular"] += 1
            return new_cell
        elif "Posterior" not in zones: #Not represented in dataset
            new_cell = Point(cell_coords, color="teal", radius=10, alpha=2.5)
            zonal_colors["Anterior, Central, Nodular"] = "teal"
            if "Anterior, Central, Nodular" not in zonal_count:
                zonal_count["Anterior, Central, Nodular"] = 1
            else:
                zonal_count["Anterior, Central, Nodular"] += 1
            return new_cell
        elif "Nodular" not in zones:
            new_cell = Point(cell_coords, color="#592720", radius=10, alpha=2.5)
            zonal_colors["Anterior, Central, Posterior"] = "#592720"
            if "Anterior, Central, Posterior" not in zonal_count:
                zonal_count["Anterior, Central, Posterior"] = 1
            else:
                zonal_count["Anterior, Central, Posterior"] += 1
            return new_cell
    else:
        if "Anterior" in zones and "Central" in zones: #Not represented in dataset
            new_cell = Point(cell_coords, color="lightgreen", radius=10, alpha=2.5)
            zonal_colors["Anterior, Central"] = "lightgreen"
            if "Anterior, Central" not in zonal_count:
                zonal_count["Anterior, Central"] = 1
            else:
                zonal_count["Anterior, Central"] += 1
            return new_cell
        elif "Anterior" in zones and "Posterior" in zones: #Not represented in dataset
            new_cell = Point(cell_coords, color="plum", radius=10, alpha=2.5)
            zonal_colors["Anterior, Posterior"] = "plum"
            if "Anterior, Posterior" not in zonal_count:
                zonal_count["Anterior, Posterior"] = 1
            else:
                zonal_count["Anterior, Posterior"] += 1
            return new_cell
        elif "Anterior" in zones and "Nodular" in zones: #Not represented in dataset
            new_cell = Point(cell_coords, color="cerulean", radius=10, alpha=2.5)
            zonal_colors["Anterior, Nodular"] = "cerulean"
            if "Anterior, Nodular" not in zonal_count:
                zonal_count["Anterior, Nodular"] = 1
            else:
                zonal_count["Central, Posterior"] += 1
            return new_cell
        elif "Central" in zones and "Posterior" in zones: 
            new_cell = Point(cell_coords, color="#e34234", radius=10, alpha=2.5)
            zonal_colors["Central, Posterior"] = "#e34234"
            if "Central, Posterior" not in zonal_count:
                zonal_count["Central, Posterior"] = 1
            else:
                zonal_count["Central, Posterior"] += 1
            return new_cell
        elif "Central" in zones and "Nodular" in zones:
            new_cell = Point(cell_coords, color="#ace1af", radius=10, alpha=2.5)
            zonal_colors["Central, Nodular"] = "#ace1af"
            if "Central, Nodular" not in zonal_count:
                zonal_count["Central, Nodular"] = 1
            else:
                zonal_count["Central, Nodular"] += 1
            return new_cell
        elif "Posterior" in zones and "Nodular" in zones:
            new_cell = Point(cell_coords, color="#0000cd", radius=10, alpha=3)
            zonal_colors["Posterior, Nodular"] = "#0000cd"
            if "Posterior, Nodular" not in zonal_count:
                zonal_count["Posterior, Nodular"] = 1
            else:
                zonal_count["Posterior, Nodular"] += 1
            return new_cell

# Adds cells to scene
def add_points(scene, cells):
    for cell in cells:
        scene.add(cell)

# Adds cell coordinate labels to scene
def add_cell_labels(scene, cell, x, y, z):
    scene.add_label(cell, str([x, y, z]), size=120, zoffset=-170)

# Adds cell coordinate labels to scene
def add_cell_name_labels(scene, cell, name):
    scene.add_label(cell, name, size=120, zoffset=-170)

# Adds the lobules to the scene rendering
def add_lobules(scene, list_of_lobules, zone_color):
    actors = []
    for lobule in list_of_lobules:
        lob = scene.add_brain_region(lobule, alpha=0.1, color=zone_color)
        actors.append(lob)
    return actors

# Setting up scene
scene = b.Scene(title="3D Rendering of Cerebellar CN Neurons")

# Adding cerebellum rendering region
cerebellum = scene.add_brain_region("CB", alpha=0.05) #mesh type
cn = scene.add_brain_region("CBN", alpha=0.05, color="grey")
fn_rendered = scene.add_brain_region('FN', alpha=0.1, color="grey")

# Adding the four zones
zone1_lobs = add_lobules(scene, zone1, "navy")
zone2_lobs = add_lobules(scene, zone2, "orange")
zone3_lobs = add_lobules(scene, zone3, "red")
zone4_lobs = add_lobules(scene, zone4, "mint")

#coordinates = set_n_points(cerebellum, 5)

# Add points (& optional coordinate labels)
cells = all_cells()
render_cells = []

for c in cells:
    x = c['x']
    y = c['y']
    z = c['z']
    zones = c['zones']
    if x != 'None' and y != 'None' and z != 'None':
        cell = create_point(x, y, z, zones)
        render_cells.append(cell)

add_points(scene, render_cells)

#add_cell_name_labels(scene, cell_2021_03_05_4, "cell_2021_03_05_4")
#add_cell_labels(scene, cell1, 11715, 4000, 7500)
#add_cell_labels(scene, cell2, 11715, 3000, 7500)

#scene.slice('frontal')
#scene.slice('frontal')

# Get color and cell count per pattern legend and save in html file as png
color_legend = open("color_count_legend.html", "w")
color_legend.write("<html>")

for k in zonal_colors:
    if zonal_count[k] == 1:
        message = k + " (" + str(zonal_count[k]) + """ cell)     <svg width="20" height="20">
        <rect width="20" height="20" style="fill:""" + zonal_colors[k] + """;stroke-width:3;stroke:rgb(0,0,0)" />
        </svg><br>"""
    else:
        message = k + " (" + str(zonal_count[k]) + """ cells)     <svg width="20" height="20">
        <rect width="20" height="20" style="fill:""" + zonal_colors[k] + """;stroke-width:3;stroke:rgb(0,0,0)" />
        </svg><br>"""
    color_legend.write(message)

color_legend.write("</html>")
color_legend.close()

imgkit.from_file('color_count_legend.html', 'color_count_legend.jpg')

# Sagittal slicing of ~1000um (Need to determine correct z start & end positions for pos and change to 300um)
plane1 = scene.atlas.get_plane(pos=[12000,4000,-5000], norm=[0, 0, 1])# plane="sagittal")
scene.slice(plane1, actors=[cerebellum, cn, fn_rendered]+zone1_lobs+zone2_lobs+zone3_lobs+zone4_lobs, close_actors=True)

plane2 = scene.atlas.get_plane(pos=[12000,4000,-4000], norm=[0, 0, -1])# plane="sagittal")
scene.slice(plane2, actors=[cerebellum, cn, fn_rendered]+zone1_lobs+zone2_lobs+zone3_lobs+zone4_lobs, close_actors=True)

# Cutting scene to only show cerebellum
plane3 = scene.atlas.get_plane(pos=[10000,4000,-5000], norm=[1, 0, 0])# plane="sagittal")
scene.slice(plane3, close_actors=True)

# Render scene
scene.content
scene.render()
