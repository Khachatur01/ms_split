# multi separator split
def ms_split(string, separators, include_separators=False):
    splits = []
    chunk = ''
    string_i = 0
    while string_i < len(string):
        is_separator = False # mark that there is no separator in current position
        for separator in separators:
            if string[string_i] == separator[0]: # if current char of string is start of any separator
                is_separator = True # temporarily mark that there is separator in this position
                for sep_i in range(1, len(separator[1:])): # iterate over separator rest chars, to find fully matching separator
                    # check if index of string is out of string range
                    # and if it is, check if last chunk is not separator
                    # or if current char of separator is not equals to appropriate char of string 
                    
                    if string_i + sep_i >= len(string) and sep_i + 1 != len(separator) or \
                        separator[sep_i] != string[string_i + sep_i]:
                        
                        # if it is mark that current position is not current separator
                        is_separator = False
                        break

                # if there is appropriate separator in current position of string
                if is_separator:
                    splits.append(chunk)
                    chunk = ''
                    string_i += len(separator)
                    if include_separators:
                        splits.append(separator)
                    break
        
        # if not found any separator
        if not is_separator:
            chunk += string[string_i]
            string_i += 1

    # add last chunk to list
    splits.append(chunk)

    return splits

splitted_list = ms_split('.abc,defg...hijklm...nopqrst.ov:wxyz.', [',', '...', '.', ':'], True)
print(splitted_list)
