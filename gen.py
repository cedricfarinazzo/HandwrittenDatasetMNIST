from mnist import MNIST
from PIL import Image, ImageDraw

def export(images, labels, bin):
    len_imgs = len(images)
    for i in range(len(images)):
        output = Image.new("L", (28, 28))
        output.putdata(images[i])
        output.save(bin + str(labels[i]) + "_" + str(i) + ".png")
        print(bin + str(labels[i]) + "_" + str(i) + ".png")


def main():
    # Load dataset
    mndata = MNIST('./mnist/', gz=True)
    tri, trl = mndata.load_training()
    tei, tel = mndata.load_testing()
    
    print("     TRAINING \n")
    export(tri, trl, './bin/training/')
    
    print("     TESTING \n")
    export(tei, tel, './bin/testing/')
    
    print("Done")
    
if __name__ == "__main__":
    main()