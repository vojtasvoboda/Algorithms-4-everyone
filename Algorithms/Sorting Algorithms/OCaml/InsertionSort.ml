let rec insertionsort = function
    | [] -> []
    | x :: l -> insert x (insertionsort l)
  and insert elem = function
    | [] -> [elem]
    | x :: l -> if elem < x then elem :: x :: l
                else x :: insert elem l
