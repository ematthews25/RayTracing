from .abcd import *
from .objectives import *
from .axicon import *
from .thorlabs import *

path = ImagingPath()
path.label = "Simple demo: one infinite lens f = 5cm"
path.append(Space(d=10))
path.append(Lens(f=5))
path.append(Space(d=10))
path.display()
# or
# path.save("Figure 1.png")

path = ImagingPath()
path.label = "Simple demo: two infinite lenses with f = 5cm"
path.append(Space(d=10))
path.append(Lens(f=5))
path.append(Space(d=20))
path.append(Lens(f=5))
path.append(Space(d=10))
path.display()
# or
# path.save("Figure 2.png")

path = ImagingPath()
path.label = "Finite lens"
path.append(Space(d=10))
path.append(Lens(f=5, diameter=2.5))
path.append(Space(d=3))
path.append(Space(d=17))
path.display()

path = ImagingPath()
path.label = "Simple demo: Aperture behind lens"
path.append(Space(d=10))
path.append(Lens(f=5))
path.append(Space(d=3))
path.append(Aperture(diameter=3))
path.append(Space(d=17))
path.display()
# or
# path.save("Figure 3.png")

path = ImagingPath()
path.label = "Microscope system"
#   path.objectHeight = 0.1
path.append(Space(d=4))
path.append(Lens(f=4, diameter=0.8, label='Obj'))
path.append(Space(d=4 + 18))
path.append(Lens(f=18, diameter=5.0, label='Tube Lens'))
path.append(Space(d=18))
path.display(onlyChiefAndMarginalRays=True, limitObjectToFieldOfView=True)
#path.save("MicroscopeSystem.png", onlyChiefAndMarginalRays=True,
#          limitObjectToFieldOfView=True)
# or
# path.save("Figure 4.png")

path = ImagingPath()
path.label = "Focussing through a dielectric slab"
path.append(Space(d=10))
path.append(Lens(f=5))
path.append(Space(d=3))
path.append(DielectricSlab(n=1.5, thickness=4))
path.append(Space(d=10))
path.display()

path = ImagingPath()
path.label = "Object at 2f, image at 2f"
path.append(Space(d=10))
path.append(Lens(f=5))
path.append(Space(d=10))
path.display()
#path.save('Figure1.png')

path = ImagingPath()
path.label = "Object at 4f, image at 4f/3"
path.append(Space(d=20))
path.append(Lens(f=5))
path.append(Space(d=10))
path.display()
#path.save('Figure2.png')

path = ImagingPath()
path.label = "Object at f/2, virtual image at -2f"
path.append(Space(d=2.5))
path.append(Lens(f=5))
path.append(Space(d=10))
path.display()
#path.save('Figure2.png')

path = ImagingPath()
path.label = "4f system with 1:1 magnification"
path.append(Space(d=5))
path.append(Lens(f=5))
path.append(Space(d=10))
path.append(Lens(f=5))
path.append(Space(d=5))
path.display()
#path.save('Figure3.png')

path = ImagingPath()
path.fanAngle = 0.1
path.append(Space(d=40))
path.append(Lens(f=-10, label='Div'))
path.append(Space(d=4))
path.append(Lens(f=5, label='Foc'))
path.append(Space(d=18))
focal = -1.0/path.transferMatrix().C
path.label = "Retrofocus system with f={0:.2f} cm".format(focal)
path.display()

path = ImagingPath()
path.label = "Thick diverging lens"
path.objectHeight = 20
path.append(Space(d=50))
path.append(ThickLens(R1=-20, R2=20, n=1.55, thickness=10, diameter=25, label='Lens'))
path.append(Space(d=50))
path.display(onlyChiefAndMarginalRays=True)

path = ImagingPath()
path.label = "Thick diverging lens, made from individual elements"
path.objectHeight = 20
path.append(Space(d=50))
path.append(DielectricInterface(R=-20, n1=1.0, n2=1.55, diameter=25, label='Front'))
path.append(Space(d=10, diameter=25, label='Lens'))
path.append(DielectricInterface(R=20, n1=1.55, n2=1.0, diameter=25, label='Back'))
path.append(Space(d=50))
path.display(onlyChiefAndMarginalRays=True)

path = ImagingPath()
path.label = "Microscope system"
path.objectHeight = 0.1
path.append(Space(d=1))
path.append(Lens(f=1, diameter=0.8, label='Obj'))
path.append(Space(d=19))
path.append(Lens(f=18,diameter=5.0, label='Tube Lens'))
path.append(Space(d=18))
path.append(Aperture(diameter=2))
path.display(onlyChiefAndMarginalRays=True, limitObjectToFieldOfView=True)
(r1,r2) = path.marginalRays(y=0)
print(r1, r2)


M1 = Space(d=10)
M2 = Lens(f=5)
M3 = M2*M1
print(M3.forwardConjugate())


M1 = Space(d=10)
M2 = Lens(f=5)
M3 = M1*M2
print(M3.backwardConjugate())


obj = Objective(f=10, NA=0.8, focusToFocusLength=60, backAperture=18, workingDistance=2, label="Objective")
print("Focal distances: ", obj.focalDistances())
print("Position of PP1 and PP2: ", obj.principalPlanePositions(z=0))
print("Focal spots positions: ", obj.focusPositions(z=0))
print("Distance between entrance and exit planes: ", obj.L)

path1 = ImagingPath()
path1.fanAngle = 0.0
path1.fanNumber = 1
path1.rayNumber = 15
path1.objectHeight = 10.0
path1.label = "Path with objective"
path1.append(Space(180))
path1.append(obj)
path1.append(Space(10))
path1.display()

path2 = ImagingPath()
path2.fanAngle = 0.0
path2.fanNumber = 1
path2.rayNumber = 15
path2.objectHeight = 10.0
path2.label = "Path with LUMPLFL40X"
path2.append(Space(180))
path2.append(LUMPLFL40X())
path2.append(Space(10))
path2.display()

print(AC254_050_A())
print(AC254_045_A())
