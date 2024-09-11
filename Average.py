from typing import List
def collectNumbers(totalNumbers:int)->List[float]:
    List_of_num=[float(input(f"Enter the number {i+1}: ")) for i in range(0,total_Numbers)]
    return List_of_num

def getAvg(number_list:List[float])->float:
    total=sum(abs(num) for num in number_list)
    return total/len(number_list)

total_Numbers=int(input("Enter the total number of numbers that you want to get average: "))
List_of_numbers=collectNumbers(total_Numbers)

avg=getAvg(List_of_numbers)
print("Average of Numbers: ",avg)