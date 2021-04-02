What is a the CSV? :-) It's a format very often use, Microsoft Excel is using it. 

It's a 2d array: ****ROW**** and ****COLUMN**** . ****Row**** are separated by "line" (the character " ") and columns are separated by ",". (Separator can be different, it can also be ";")

Your mission here, is to transform a string following the CSV format to a 2d array.

Your function will takes two arguments, the content of a CSV as a string and a separator. Your function will return an arrays (lines) of arrays (columns).

	##
	##
	## QWASAR.IO -- my_csv_parser
	##
	##
	## @param {String} param_1
	## @param {String} param_2
	##
	## @return {string[][]}
	##
	
	
	def my_csv_parser(param_1, param_2)
		
	end

****EXAMPLE:****

	Input: "a,b,c,e\n1,2,3,4\n" && ","
	Output: 
	Return Value: [["a", "b", "c", "e"], ["1", "2", "3", "4"]]


