def my_csv_parser(param_1, param_2 = ",")
    param_1.split("\n").map! do |row|
        row.split(param_2)
    end
end
