'''
This module compresses and deompresses text files with Huffman encoding
It is a lossless algorithm.
'''
from bitstring import BitArray
import sys
import pickle
from tqdm import tqdm, trange

codes = {} #codes dictionary


def copied_string(filename_code):
    '''
    A function to return the whole string copied from
    the file opened
    '''
    original_string =''
    lines = filename_code.readlines()
    for line in lines:
        for i in lines:
            original_string+=i
    return original_string
    
def frequency_of_chars(str)-> str:
    '''
    A function to determine the frequencies of each character in the string
    Arguments: str - String
    Returns: freqs - dictionary
    '''
    print("\nChecking frequencies...")
    freqs = {}
    for char in str:
        freqs[char] = freqs.get(char,0)+1
    return freqs

def sort_frequency(freqs)-> dict:
    '''
    Sorts the frequencies from high to low
    Arguments: freqs - Dictionary of frequencies
    Returns: tuples - list
    '''
    print("\nSorting frequencies...")
    letters = freqs.keys()
    tuples = []
    for i in letters:
        tuples.append((freqs[i], i))
    tuples.sort()
    return tuples

def build_tree(tuples)-> list:
    '''
    Builds the trees based on the frequencies of the characters
    Arguments: tuples - list
    Retutns tuples[0] - tree built inside the list
    '''
    print("\nBuilding tree...")
    while len(tuples) > 1:
       leastTwo = tuple(tuples[0:2]) #getting the two smallest to combine
       theRest = tuples[2:] #assigning everything else
       combFreq = leastTwo[0][0] + leastTwo[1][0] #combining the frequency
       tuples = theRest + [(combFreq,leastTwo)] #adding branch point
       tuples = sorted(tuples, key=lambda x: x[0])
    return tuples[0] #return the single tree inside the list

def trim_tree(tree)-> list:
    '''
    Takes away the frequency counter leaving just the tree
    Arguments: tree - list (the tree)
    Returns: trimmed tree
    '''
    p = tree[1]
    if isinstance(p, str):
        return p
    return trim_tree(p[0]), trim_tree(p[1])

def assign_codes(node, code=''):
    '''
    Recursively assigns codes based on the tree
    Arguments: node - for each node in the list a string is assigned
               pat - used by the recursion to build a string 
    '''
    if isinstance(node, str):
        codes[node] = code #assigns the string to the node
    else: #enters recursion until node is met
        assign_codes(node[0], code+"0") #if the left branch is taken then 0 is added to the string
        assign_codes(node[1], code+"1") #if the right branch is taken then a 1 is added to the string
        
   
def encoding(string)->str:
    '''
    Encodes the string using the codes dictionary
    Arguments: string - String to be compressed
    Returns: compressed version of the string
    '''
    print("\nEncoding...")
    compressed_string = ''
    for i in string:
        compressed_string += codes[i]
    return compressed_string

def decoding(tree, string):
    '''
    Decodes a string based on the given tree and the
    encoded string
    Arguments: tree - tree for the given compressed string
               string - compressed binary string
    Returns: decompressed string
    '''
    decompressed_string = ''
    p = tree
    for num in string:
        if num == '0':
            p = p[0]
        else:
            p = p[1]
        if isinstance(p,str):
            decompressed_string+=p
            p=tree
    return decompressed_string

#This section is the main method of the module and takes in user arguments
try:
    if sys.argv[1]=="compress" and sys.argv[2].endswith(".txt") and sys.argv[3].endswith(".bin"):
        print("Compressing file " + sys.argv[1] + " to file " + sys.argv[3] + "...")
        pbar = tqdm(total=100)
        original_string=''
        txt_file = open(sys.argv[2], encoding='utf8') #opens the file specified by the user
        print("\nBuilding string...")
        original_string = copied_string(txt_file)
        pbar.update(20)
        #the code below makes the compressed array ready to be written to a .bin file
        freqs = frequency_of_chars(original_string)
        sortedFreqs = sort_frequency(freqs)
        pbar.update(10)
        built_tree = build_tree(sortedFreqs)
        tree = (trim_tree(built_tree))
        pbar.update(10)
        final_codes = assign_codes(tree)
        compressed_string = encoding(original_string)
        pbar.update(10)
        compressed_array = BitArray(bin=compressed_string) #makes a BitArray of the string
        pbar.update(10)
        with open(sys.argv[3], 'wb+') as f: #makes a .bin file named by the user
            serial_tree = pickle.dumps(tree) #serialises the tree
            pbar.update(10)
            serial_tree_length = len(serial_tree)
            serial_compressed_array = pickle.dumps(compressed_array) #serialises the array
            pbar.update(10)
            serial_compressed_array_length = len(serial_compressed_array)
            #this section makes the header of the file (4 bytes long) 
            header = bytearray(b'\xAF\x00\xAF\x00')
            full_header = header + serial_tree_length.to_bytes(4,byteorder='big') + serial_compressed_array_length.to_bytes(4, byteorder='big') + header
            f.write(full_header + serial_tree + serial_compressed_array)
            pbar.update(20)
        pbar.close()
        print("Compressing complete")
    elif sys.argv[1]=="decompress" and sys.argv[2].endswith(".bin") and sys.argv[3].endswith(".txt"):
        print("Decompressing "+ sys.argv[2] + " to file " + sys.argv[3] + "...")
        pbar = tqdm(total=100)
        with open(sys.argv[2], 'rb') as f:
            header_check = f.read(4) 
            #write a check for 0xafx00xafx00
            length_of_tree = f.read(4)
            length_of_tree_int = int.from_bytes(length_of_tree, 'big')
            pbar.update(10)
            #convert to decimal
            length_of_compress = f.read(4)
            length_of_compress_int = int.from_bytes(length_of_compress,'big')
            pbar.update(10)
            #trailer check
            check_trail = f.read(4)
            #check trail is same as original header start
            tree_read = f.read(length_of_tree_int)
            recovered_tree = pickle.loads(tree_read)
            compressed_read = f.read(length_of_compress_int)
            downloaded_compressed_array = pickle.loads(compressed_read)
            pbar.update(30)
            

        downloaded_compressed_array = downloaded_compressed_array.bin
        decoded_string = decoding(recovered_tree, downloaded_compressed_array)
        pbar.update(30)
        with open(sys.argv[3], 'wt+', encoding='utf8') as txt:
            txt.write(decoded_string)
        pbar.update(20)
        pbar.close()
        print("Decompression complete...")
    else:
        print("Please enter the correct number of arguements(command, original file, new file)")
except Exception as e:
    print("There was an error.")
    print("Please enter the correct number of arguements(command, original file, new file)")
