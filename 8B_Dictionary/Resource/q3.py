#Part A
def encrypt(dict, msg):
    return str()

# Part B
def decrypt(dict, msg):
    return str()

if __name__ == "__main__":
    # Part A
    cipher_dict = {'a':'n', 'b':'o', 'c':'p',
             'd':'q', 'e':'r', 'f':'s',
             'g':'t','h':'u','i':'v',
             'j':'w', 'k':'x','l':'y',
             'm':'z','n':'a','o':'b',
             'p':'c','q':'d','r':'e',
             's':'f','t':'g','u':'h',
             'v':'i', 'w':'j','x':'k',
             'y':'l','z':'m'}

    print('\nTestcase')
    print('-' * 10)
    print("Expected: v ybir clguba")
    msg = 'i love python'
    print("Actual  : " + encrypt(cipher_dict, msg))


    # Part B
    print('\nTestcase')
    print('-' * 10)
    msg = 'v ybir clguba'
    print("Expected: i love python")
    print("Actual  : " + decrypt(cipher_dict, msg))