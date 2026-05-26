# Challenge 1: Sorting

def sorted_separated(sequence):
    liste = sequence.split(",")
    print("sequence transformée en liste: ",liste)
    liste.sort()
    print("liste ordonnée: ",liste)

    return ",".join(liste)

print(sorted_separated("without,hello,bag,world"))

# Challenge 2

def longest(sentence):
    new_sentence = sentence.split(" ")
    long = new_sentence[0]
    for word in sentence:
        if len(word) > len(long):
            long = word
    
    return long

print(longest("Margaret's toy is a pretty doll."))
