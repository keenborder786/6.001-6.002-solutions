l=int(input("What size will your require "))
def drawtheboard(l):
        for num in range(l):
            print("| |"*l)
def is_winner(matrix):
    x=1
    y=2
    i=0
    a=matrix[0]
    b=matrix[1]
    c=matrix[2]
    for char in a:
        if char==b[i]==c[i]==x:
            print("Player x wins")
            break
        elif char==b[i]==c[i]==y:
            print("Player y wins")
            break
        i+=1 
    #other wining condition for 3*3 matrix are below
    if a[0]==b[1]==c[2]==x:
        print("Player x wins")
    elif a[2]==b[1]==c[0]==x:
        print("Player x wins")
    elif a[0]==b[1]==c[2]==y:
        print("Player y wins")
    elif a[2]==b[1]==c[0]==y:
        print("Player y wins") 
    elif a[0]==a[1]==a[2]==x:
          print("Player x wins")
    elif a[0]==a[1]==a[2]==y:
          print("Player y wins")
    elif b[0]==b[1]==b[2]==x:
         print("Player x wins")
    elif b[0]==b[1]==b[2]==y:
          print("Player y wins")
    elif c[0]==c[1]==c[2]==x:
          print("Player x wins")
    elif c[0]==c[1]==c[2]==y:
          print("Player y wins")
    else:
        print("This is a draw")
matrix=[[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]         
is_winner(matrix)  
def user_input(matrix):
    matrix = [[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]
    Q=1
    a=matrix[0]
    b=matrix[1]
    c=matrix[2]
    while Q<10:
        row_col_old=input("Please enter your input:player x,please note that you have to input two value:row,coloum")
        row_col_new=row_col_old.split(",")
        if row_col_new[0]=="1":
            for i in range(3):
                if row_col_new[1]==str(i+1) and a[i]!="O" and a[i]!="X" :
                    a[i]="X"
        elif row_col_new[0]=="2":
            for i in range(1,4,1):
                if row_col_new[1]==str(i) and b[i-1]!="O" and b[i-1]!="X":
                    b[i-1]="X"
        elif row_col_new[0]=="3":
            for i in range(1,4,1):
                if row_col_new[1]==str(i) and c[i-1]!="O" and c[i-1]!="X":
                    c[i-1]="X"
        row_col_old=input("Please enter your input:player y,please note that you have to input two value:row,coloum")
        row_col_new=row_col_old.split(",")
        if row_col_new[0]=="1":
            for i in range(3):
                if row_col_new[1]==str(i+1) and a[i]!="O" and a[i]!="X":
                    a[i]="O"
        elif row_col_new[0]=="2":
            for i in range(1,4,1):
                if row_col_new[1]==str(i) and b[i-1]!="O" and b[i-1]!="X":
                    b[i-1]="O"
        elif row_col_new[0]=="3":
            for i in range(1,4,1):
                if row_col_new[1]==str(i) and c[i-1]!="O" and c[i-1]!="X":
                    c[i-1]="O"
        else:
            print("Please enter a valid value")
            Q-=1
        Q+=1
        print(a,b,c)    
matrix = [[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]
user_input(matrix)               
            
            
       
        
        
