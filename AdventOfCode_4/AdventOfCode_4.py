import hashlib

## returns the requested number of leading digits 
## for the md5 hash of a given key

def md5_hash_string(key, num_positions):
    full_hash = hashlib.md5(key).hexdigest()
    leading_positions = int(full_hash[0:num_positions], 16)
    return leading_positions

## concatanates the given secret key with an incrementing integer, until 
## the md5 hash result has the requisite number of leading zeroes

def find_match(key_first_half, num_zeroes):
    key_second_half = 0

    while (1):
        key = key_first_half + str(key_second_half)

        if (md5_hash_string(key, num_zeroes) == 0):
            print "The answer for %d zeroes is: %d." % (num_zeroes, key_second_half)
            break
        else:
            key_second_half += 1    

def main(key_first_half, leading_zeroes, ending_num_zeroes):
    
    while (leading_zeroes <= ending_num_zeroes):
        find_match(key_first_half, leading_zeroes)
        leading_zeroes += 1

main("yzbqklnj", 5, 6)