# display  * on screen

from tkinter.messagebox import NO


def display(No):

    for x in range(0,No):
        print("*",end=" ")



def main():
    print("Enter number")
    No=int(input())

    display(No)





if __name__ == "__main__":
    main()