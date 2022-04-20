import brainrender as b

cb = 'CB'
fn = 'FN'
ip = 'IP'
dn = 'DN'

# Rendering settings
b.settings.WHOLE_SCREEN = False
b.settings.SHADER_STYLE = "plastic"
b.settings.ROOT_ALPHA = 0.05

# Setting up scene
scene = b.Scene(title="3D Rendering of CN Components")

# Adding CN rendering regions
cerebellum = scene.add_brain_region(cb, alpha=0.15)
fn_rendered = scene.add_brain_region(fn, alpha=0.25, color="red")
ip_rendered = scene.add_brain_region(ip, alpha=0.25, color="green")
dn_rendered = scene.add_brain_region(dn, alpha=0.25, color="blue")

fn_rendered.wireframe()
ip_rendered.wireframe()
dn_rendered.wireframe()

# Printing out region actor details. "Dimensions" show the coordinate bounds for the regions. LR is currently showing bounds that include both nuclei.
print(fn_rendered)
print(ip_rendered)
print(dn_rendered)

# Saving CN coordinate data to a new txt file
print(fn_rendered, file=open("CN_data.txt", "w"))
print(ip_rendered, file=open("CN_data.txt", "a"))
print(dn_rendered, file=open("CN_data.txt", "a"))

# Cutting scene to only show cerebellum
scene.slice('frontal')
scene.slice('frontal')

# Render scene
scene.content
scene.render()