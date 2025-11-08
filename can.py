import math
def main():
    name="#1 picnic"
    radius=6.83
    height=10.16
    can_eff(name,radius,height)

    name="#1 tall"
    radius=7.78
    height=11.91
    can_eff(name,radius,height)

def can_eff(name, radius, height):
    volume = can_vol(radius, height)
    area = can_area(radius, height)
    eff = volume / area
    print("")
    print(f"{name} volume={volume:.2} area={area:.2} efficiency={eff:.2}")

def  can_vol(radius, height):
    volume = math.pi * radius ** 2 * height
    return volume

def can_area(radius, height):
    area = 2 * math.pi * radius * (radius + height)
    return area
main()