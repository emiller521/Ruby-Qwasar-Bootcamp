def my_hamming_dna(dna_1,dna_2)
    str1=dna_1.split("")
    str2=dna_2.split("")
    hamming_count=0
    if(str1.length == str2.length)
        str1.each_index do |idx|
                hamming_count += 1 if
                str1.values_at(idx) != str2.values_at(idx)
        end
    else
        hamming_count = -1
    end

    return hamming_count


end
