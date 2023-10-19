import hashlib

def crack_sha1_hash(hash, use_salts = False):
    file_path = 'top-10000-passwords.txt'
    salts_file_path = 'known-salts.txt'
    
    solved_password = None
        # Iterate through each line (each line is a password)
        # Break it down into salted version and unsalted version of code
    with open(file_path, 'r') as file:
        if use_salts == True:
            for line in file:
                password = line.strip()
                with open(salts_file_path, 'r') as file2:
                    for line2 in file2:
                        salt = line2.strip()
                        salted_password_append = salt + password
                        salted_password_prepend = password + salt
                        hashed_password_append = sha1_hash(salted_password_append)
                        hashed_password_prepend = sha1_hash(salted_password_prepend)
                        if hashed_password_append == hash or hashed_password_prepend == hash:
                            solved_password = password
                            break
                        
            
        else:
            #UnSalt Code
            for line in file:
                password = line.strip()
                hashed_password = sha1_hash(password)

                if hashed_password == hash:
                    solved_password = password
                    break
    
    if solved_password is None:
      return "PASSWORD NOT IN DATABASE"
    else: 
      return solved_password
    

def sha1_hash(string_to_hash):
    input_string = str(string_to_hash)
    #Creating a new SHA-1 hash object
    sha1 = hashlib.sha1()
    #Updating the hash object with input string
    sha1.update(input_string.encode('utf-8'))
    #Getting the hexadecimal digest of the hashed input
    hashed_string = sha1.hexdigest()

    return hashed_string