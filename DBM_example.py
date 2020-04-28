import dbm
import pickle
db = dbm.open('captions', 'c')

# When you create a new item in the db, dbm updates the database file
db['cleese.png'] = 'Photo of John Cleese.'     # Store string into the db

# When you access one of the items, dbm reads the db file:
print(db['cleese.png'])                        # Display the value in the db
## b'Photo of John Cleese.'
# The result is a bytes (string) object, which is why it begins with b.

#------------------------------------------------------------------------------

# If you make another assignment to an existing key, dbm replaces the old value:
db['cleese.png'] = 'Photo of John Cleese doing a silly walk.'
print(db['cleese.png'])
## 'Photo of John Cleese doing a silly walk.'

#------------------------------------------------------------------------------

# Example of using pickling on numbers to store their values into a db
t1 = [1, 2, 3]
s1 = pickle.dumps(t1)                  # Dump string (pickle) the numberic list into a byte string
print("\nList =", t1)                  # Display the original list
print("Pickle List original =\t", s1)  # Display the byte string (pickled)
db['answers'] = s1                     # Store the pickled byte string in the db

s2 = db['answers']                     # Retrieve the byte string from the db
t2 = pickle.loads(s2)                  # Load the byte string (reconstitute) into a numberic list
print("\nPickle list from db =\t", s2) # Display the retrieved byte string from the db
print("List from db =", t2)            # Display numeric list from the reconstituted byte string

db.close()