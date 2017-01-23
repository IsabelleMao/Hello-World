input_for_sorting = input("Paste in (or type, I won't judge) a list of things you'd like to be sorted!")
split_input = input_for_sorting.split()

for index in range(len(split_input)):
  for index in range(len(split_input)):
    if split_input[index] < split_input[index - 1] and split_input[index-1] != split_input[-1]: #if current one is earlier in the alphabet than the previous one
      swap_down = split_input[index - 1]
      swap_up = split_input[index]
      split_input[index] = swap_down
      split_input[index-1] = swap_up
    
for index in range(len(split_input)):
  print(split_input[index])
