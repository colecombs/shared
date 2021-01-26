# functions for testing

def first_half(s):
    return s[:len(s)//2]  # must use // to return an integer, a single slash will return a float
def last_half(s):
    return s[len(s)//2:]

# We are currently running this script

if __name__ == '__main__':
    print("Testing string functions")
    assert first_half("abcd") == "ab" , "First half is failing"
    assert last_half("abcd") == "cd" , "Last half is failing"
