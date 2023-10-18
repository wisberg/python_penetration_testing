import hashlib

def crack_sha1_hash(hash):
    #In this project, we are comparing hashed passwords to a hash we are given. 
    #My basic gameplan is to take the hash I am given, and compare it to the top - 10000 passwords hashed to see if they are the same
    #I will hash the top 10000 passwords, compare to the hash, and if they are the same I have cracked the password
    # Open the file containing the passwords
    file_path = 'top-10000-passwords.txt'  # Replace with the actual path to your file
    solved_password = None
    with open(file_path, 'r') as file:
        # Iterate through each line (each line is a password)
        for line in file:
            # Remove any leading or trailing whitespace, such as newlines
            password = line.strip()
        
            # Now, you can process each password, for example, by calling your hash function
            hashed_password = sha1_hash(password)
        
            # Then, you can compare the hashed_password with the target hash
            if hashed_password == hash:
                solved_password = password
                break  # If you've found the password, you can exit the loop

    if solved_password == None: 
        print('PASSWORD NOT IN DATABASE')
    else: 
        print(solved_password)
    return 0
    

def sha1_hash(string_to_hash):
    # Your input string
    input_string = str(string_to_hash)
    # Create a new SHA-1 hash object
    sha1 = hashlib.sha1()
    # Update the hash object with your input string (encoded as bytes)
    sha1.update(input_string.encode('utf-8'))
    # Get the hexadecimal digest of the hashed input
    hashed_string = sha1.hexdigest()

    return hashed_string

crack_sha1_hash('b80abc2feeb1e37c66477b0824ac046f9e2e84a0')