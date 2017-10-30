def count_sort (array, range)

  counter = Array.new(range+1, 0) 
  # This counter array will keep track of the occurances of each item
  # We specifically set the default values to 0 for easier counting
  array.each do |item|
    counter[item] += 1 # Increase count for each occurance
  end

  # Now we modify the counter to store the sum of counts
  (1...counter.size).each do |index|
    # This will give us the object positions when we make the output array
    counter[index] = counter[index] + counter[index-1] 
  end

  # Now we make the output array
  result = Array.new(array.size)
  for i in 0...array.size do
    counter[array[i]] -= 1
    result[counter[array[i]]] = array[i]
  end

  result
end