def res():
  z = [" "]
  i = int(input("How many numbers do you have? "))
  if i <= 1:
    print("ammount of your numbers must be bigger than 1")
    res()
  else:
    for j in range (i):
      in_num = int(input("Please enter your number: "))
      z.insert(0, in_num)
    else:
      z.remove(" ")
      nums = set(z)
      print(str(max(nums)) + " is your biggest number and " + str(min(nums)) + " is your smalles number.")
      print(str(nums) + " is your numbers")
      
      sorted = [""]

      for i in range(len(nums)):
        sorted.insert(0, (max(nums), [i + 1]))
        nums.remove(max(nums))
      else:
        sorted.remove("")
        print(str(sorted) + " is sorted list of your numbers. USER GUIDE: (Number[ranking]).")
    
    ask = str(input("Do you want to run code again? any letter for running again, [n] for refusing from running again: "))
    if ask == "n":
      print("the end")
    else:
      res()
res()