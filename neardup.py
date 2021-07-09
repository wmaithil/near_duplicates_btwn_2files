                                                                                                                               import sys

# Function to calculate finger prints representing a Document
def nearDuplicate(foo):

    #List of Empty Hash Values
    sums=[]

    #For loop parsing document text and filling sums list with the hash values 
    for i in range(0,len(foo)-1):
        sum = 0
        fooBar = ' '.join(foo[i:i+3])   # n-grams for n = 3
        for s in fooBar:
            sum += ord(s)
        sums.append(sum)

    # returning Selected Hash Values as fingerprints Using '0 mod 4'
    hash = [i for i in sums if i%4==0]
    return hash

#Usage details
if len(sys.argv) == 1:
    print("Usage: python3 fingerprint.py [Doc #1] [Doc #2] ")
    exit()


#Opening The FileS for Reading
bar1 = open(sys.argv[1],'r')
bar2 = open(sys.argv[2],'r')


foo1 = bar1.read().split()
foo2 = bar2.read().split()                                  

# Printing Contents of the Docs
print('\nDocuments Texts')
print('---------------------------------------------')
print("{} := {}".format(sys.argv[1],' '.join(foo1)))
print("{} := {}".format(sys.argv[2],' '.join(foo2)))
print('\n')


HashDoc_1 = nearDuplicate(foo1)
HashDoc_2 = nearDuplicate(foo2)

print("Fingerprint Hash Values Representing each Docs are: ")
print("--------------------------------------------------------")
print("{} := {}".format(sys.argv[1], HashDoc_1))
print("{} := {}".format(sys.argv[2], HashDoc_2))
print("\n")



# Calclulating number of shared fingerprintas
Shared_Count = 0

for i in HashDoc_1:
    for j in HashDoc_2:
        if i == j:
            Shared_Count += 1
            break

# Printing Similarity OR Disimilarity of input Docs
if Shared_Count == 0:
    print("Both Documents are Totally different")

elif Shared_Count == len(HashDoc_1) and Shared_Count == len(HashDoc_2) :
    print("Both Documents are Same\n")

else:
    print("Shared FingerPrint Count is: " + str(Shared_Count) + " \nHence, Docs are Near-Duplicates with similarity ratio of " + str(float(Shared_Count/max(len(HashDoc_1),len(HashDoc_2)))))


print('\n')
