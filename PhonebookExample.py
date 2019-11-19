#From 12.6 Dictionaries and tuples
# Create a phonebook dictionary that has uses a last-name, first-name
# tupple for the index into the phonebook.
# Note: You can use tuples as keys in dictionaries (primarily because you can’t use lists)

print("Phone book example using a dictionary:")
last = 'Jones'; first = 'Sam'
name = (last, first)
number = "+1 111-111-1111"

t = [(name, number)]
phonedir = dict(t)
# Add names to the phone director dictionary
phonedir["Doe", "John"] = "+1 111-111-2222"
phonedir["Doe", "Jill"] = "+1 111-111-3333"
phonedir["Smith", "Frank"] = "+1 111-222-5555"

print("Jill Doe's phone number:", phonedir["Doe", "Jill"])

print("\nDictionary lookup for Phone Directory (Entries = ", len(phonedir), "):",sep='' )
print("Name \t\t Phone Number")
for last, first in phonedir:
    print(first, last, '\t', phonedir[last,first])
