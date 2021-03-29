def my_string_index(param_1, param_2)
    checking = 0
    
    while param_1[checking] do
        if param_1[checking] == param_2
            return param_1.index(param_2)
        else 
            checking = checking + 1
        end
    end
    return -1
end
