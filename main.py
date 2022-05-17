import imageio as iio
import sys

def main():

    if len(sys.argv) == 1:
        pic = input("Enter file name: ")
    else:
        pic = sys.argv[1]

    f = open('output.txt', 'w+')

    image = iio.imread(pic)

    h = image.shape[0] #Height of the image
    w = image.shape[1] #Width of the image
    r = h/w

    print("Height:", h,"Width:", w, "Ratio:", r)

    scalar = 75 #Larger value results in higher resolution
    pennyMode = "x"
    while pennyMode != "A" and pennyMode != "P":
        pennyMode = input("ASCII art or penny mode? (A/P):")

    hstep = int(h / scalar) #Number of pixels to skip vertically
    
    if (pennyMode == "A"):
        library = "    `-.',~\"_:;^r>*?|\/Licl7vz1xt{}]Ffujy2SoaZemwXPEhk6$9qKOdHDR8MWgN#BQ"
        wstep = int(h/scalar/1.7) #step less far in the horizontal, as characters on screen are taller than they are wide
        print("Vertical Step:", int(hstep),"Horizontal Step:", wstep)

        for i in range(0, h, hstep):
            for j in range(0, w, wstep):
                f.write(convert(image[i][j], library))
            f.write('\n')
    else:
        library = "0123456789      " #low numbers are dark, high numbers are bright
        wstep = int(h/scalar*1.154) #step further in the horizontal, as tiled pennies are wider than they are tall
        print("Vertical Step:", hstep,"Horizontal Step:", wstep)
        print("Final piece:")
        print(int(h/hstep), "pennies tall by", int(w/wstep), "pennies wide")
        print("Requiring roughly", int(h/hstep)*int(w/wstep), "Pennies total")
        print(int(w/wstep)*3/48, "Feet wide,", int(h/hstep)*2.5/48, "Feet Tall")

        k = 0
        for i in range(0, h, hstep):
            if (k == 1):
                f.write(" ")
            for j in range(0, w, wstep):
                if (k == 1):
                    f.write(convert(image[i][int(j-wstep/2)], library))
                else:
                    f.write(convert(image[i][j], library))
                f.write(" ")
            k = 1- k
            f.write('\n')


def convert(val, lib):
    pixelIntensity = sum(val[0:2]) / (3 * 255)
    if (len(val) == 4): #Checks for alpha value, scales accordingly
        pixelIntensity = pixelIntensity * (val[3]/255)
    return lib[int((len(lib) - 1) * pixelIntensity)] #indexes into DENSITY proportionate to the brightness of the given pixel


if __name__ == "__main__":
    main()
