import random

  
# list of items
    List = [10, 20, 30, 40, 50, 40,
        30, 20, 10]
  
# using the sample() method
    UpdatedList = random.sample(List, 3)
  
# displaying random selections from 
# the list without repetition
    print(UpdatedList)
