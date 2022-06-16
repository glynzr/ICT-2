#Task C:Orta qiymet
n=0 #daxil edilen Letter deyiseninin sayi (bosluq nezere alinmaqla)
total_grade_points=0

while True:
    Letter=input("Enter the grade(blank to quit): ")
    n+=1

    
    if Letter=="A+" or Letter=="A":
        total_grade_points+=4.0
    elif Letter=="A-":
        total_grade_points+=3.7
    elif Letter=="B+":
        total_grade_points+=3.3
    elif Letter=="B":
        total_grade_points+=3.0
    elif Letter=="B-":
        total_grade_points+=2.7
    elif Letter=="C+":
        total_grade_points+=2.3
    elif Letter=="C":
        total_grade_points+=2.0
    elif Letter=="C-":
        total_grade_points+=1.7
    elif Letter=="D+":
        total_grade_points+=1.3
    elif Letter=="D":
        total_grade_points+=1.0
    elif Letter=="F":
        total_grade_points+=0
        
        
    if Letter==" ":
        break
average=total_grade_points/(n-1)#n-nin qiymetinde herfi qiymetlerin sayi ile beraber bosluq da nezere alindigi ucun 1 cixilir 
print("A grade point average: {}".format(average))

