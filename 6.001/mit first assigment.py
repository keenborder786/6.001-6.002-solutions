r=0.04
b=0
n=0
x=0
annual_salary=float(input("Enter your annual salary "))
total_cost=1000000
current_saving=0
down_payment=.25*total_cost
low=0
high=10000
guess=0
epsilon=100
while abs((current_saving-(down_payment))) >=1000:
    if current_saving < down_payment:
        low=guess
    else:
        high=guess
    guess=((high+low)/2)
    x=((1+r/12)**36)*(guess)/(annual_salary/12)
    current_saving= ((1+r/12)**36)*(guess) + (x*(annual_salary/12)*36)
    b+=1
    if x>1:
        print("Its impossible to saved with this salary")
        break
print("The best saving rate is:",x)
print("The bisection steps are",b)

