# Q1

## ASSUMPTIONS:

1. Every student has unique roll number
2. Search is implemented only for First Name, Last Name, Roll Number, Course Name and Exam Type
3. Updating operation is only for updating scored marks. 
4. Directory contains unique entries.   
5. Click 7 in the initial menu to exit the program, (Ctrl+C) doesn't work
6. The directory is loaded into another csv file before exiting (Based on User's choice).
7. Every entry has unique (Roll Number, Course Name, Semester, Exam Type). 

## INPUT and OUTPUT: 

1. The input & output formats are self explainatory, Please select the options as given. 

# Q2:

## ASSUMPTIONS:

1. Starting point(S) is assumed to be (0,0)

## INPUT:

1. It is required that the input is given in the format : 3mm,N
2. If required in centimenters then please follow 4cm,N
3. Use the following for directions : N = North, S = South, E = East and W = West similarly SW = SouthWest. 
4. The input process can be terminated by giving an empty input i.e., just press enter when asked for the input. 

## OUTPUT: 

1. The final point position is given as one of the 4 quadrants with S as origin. 
2. The output distance is the euclidean distance and in Millimeters. 
3. Map also has numberings on each point indicating the order of traversal. 

## Example Input and Output: 

Enter the command (For ex : 3mm,N) : 4mm,N
Enter the command (For ex : 3mm,N) : 5mm,E
Enter the command (For ex : 3mm,N) : 
Final point is Northeast of S
The euclidean distance(displacement) between S and final point is 6.4031242374328485

# Q3

## ASSUMPTIONS:

1. Crows go first. 
2. Crows can be moved only after all of them are placed. 
3. If the Vulture has a killing move then it must take it. 

## INPUT:

1. Crows can be moved after selecting by clicking on them first and placing them at the desired point. 
2. Vultures need not be selected by clicking to move them. 

## OUTPUT: 

1. The match result is displayed on the Turtle window not on the terminal. 