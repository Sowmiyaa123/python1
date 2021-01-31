test_str = input("Please enter the string:")
  
all_freq = {} 
  
for i in test_str: 
    if i in all_freq: 
        all_freq[i] += 1
    else: 
        all_freq[i] = 1
  
# printing result  
print ("Count of all characters in the given word=\n "
                                        +  str(all_freq))
