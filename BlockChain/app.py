import streamlit as st
import numpy as np
import pandas as pd
# Imports
from dataclasses import dataclass
# Creating the Block data class
from datetime import datetime
#########################################################################
from typing import Any
import hashlib
# Create an instance of the sha256 hashing function
sha = hashlib.sha256()
# # Create the data input to be hashed
# my_data = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque a nisi et nunc sollicitudin laoreet in sed neque. Proin convallis varius odio, id euismod justo tristique at. Cras at ultricies nisi, sed vulputate ante. Praesent faucibus odio in tortor tincidunt tincidunt. Vivamus interdum, tortor ac semper laoreet, nisl nibh tincidunt ante, vitae iaculis arcu sapien quis turpis. Nunc in ullamcorper enim. Sed in est egestas, pulvinar orci in, laoreet nisl."

# # Encode the data using the encode function
# encoded_data = my_data.encode()
# # Hash the encoded data
# sha.update(encoded_data)

# # Print the hash code
# print(sha.hexdigest())

##########################################################################
st.write("# Python Web App")
st.write("## This is a Test Run")
st.write("Hi, this is our first web app in Python! :sunglasses: My Boss My Hero")
df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
st.write(df)
##########################################################################
# Creating the Block data class
@dataclass
class Block:
    data: Any
    creator_id: int
    timestamp: str = datetime.utcnow().strftime("%H:%M:%S")
    def hash_block(self):
        sha = hashlib.sha256()

        # Turn the block data into an encoded string
        data = str(self.data).encode()
        sha.update(data)

        # Turn the block timestamp into an encoded string
        timestamp = str(self.timestamp).encode()
        sha.update(timestamp)

        return sha.hexdigest()

# Create a new block instance using some test data
# new_block = Block(data="test", creator_id=42)

# Calculate the block hash using the new method
# block_hash = new_block.hash_block()

# Print the block's hash
# print(block_hash)
#-------------------------------------------------------
# Create a data class called Counter
@dataclass
class Counter:
    count: int = 0
    def update_count(self):
        self.count = self.count + 1
# Create a new instance of Counter
new_counter = Counter()

# Update the count by calling update_count
new_counter.update_count()
new_counter.update_count()

# Print the updated value of count
print("The current count is: ", new_counter.count)
#-----------------------------------------------------------
# Create a method called hash_block

#-----------------------------------------------------------
input_value = st.text_input("Enter a Message")
# Encode the data using the encode function
# encoded_data = input_value.encode()
# Hash the encoded data
# sha.update(encoded_data)
# Creating a new block
new_block = Block(data=sha.hexdigest(), creator_id=168)
# Print the new block
# print(new_block)
if st.button("Display Message"):
    st.write(f"Input Value: {input_value}")
    st.write(f"Output Hash (fingerprint): {new_block}")
    st.write(f"Output Length: {len(input_value)}")