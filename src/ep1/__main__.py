#!/usr/bin/env python3
#coding=utf-8

from assignments.assignment_a import assignment_a
from assignments.assignment_b import assignment_b
from assignments.assignment_c import assignment_c

def print_assignment_header(letter):
    print("\n=====================================================================================")
    print('=================================== assignment {type} ===================================='.format(type = letter))
    print("=====================================================================================\n")

def main():
    while True:
        assignment = input("Do you want to see which assignment: ")
        if ((assignment=="a") or (assignment=="A")):
            print_assignment_header("A")
            assignment_a()

        elif ((assignment=="b") or (assignment=="B")):
            print_assignment_header("B")
            assignment_b()

        elif ((assignment=="c") or (assignment=="C")):
            print_assignment_header("C")
            assignment_c()

        else:
            print("your input isn't valid \nplease, try again\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nBetter luck next time")
