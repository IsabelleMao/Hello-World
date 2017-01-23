#Ask the user for input
input_for_sorting = input("Paste in (or type, I won't judge) a list of things you'd like to be sorted!")
split_input = input_for_sorting.split()
length_of_list = len(split_input)

#The sorter
#Sort all the words.
for index in range(length_of_list):
  #Needed for sorting just one word
  for index in range(len(split_input)):
    #If current one is earlier in the alphabet than the previous one:
    if split_input[index] < split_input[index - 1] and split_input[index-1] != split_input[-1]:
      #Swap their positions
      swap_down = split_input[index - 1]
      swap_up = split_input[index]
      split_input[index] = swap_down
      split_input[index-1] = swap_up

#Print the new list, one by one.
for index in range(length_of_list):
  print(split_input[index] + " ")
  
#https://www.youtube.com/watch?v=WaNLJf8xzC4
