path = 'Lecture\Lecture_2\example_3.txt'  #path - путь.
data=open(path,'r') 
for line in data:
    print(line)
data.close()