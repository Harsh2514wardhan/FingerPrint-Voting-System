#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import hashlib

# Simulated fingerprint database (fingerprints are represented as hashes)
fingerprint_database = {
    "voter1": "fingerprint_hash1",
    "voter2": "fingerprint_hash2",
    # Add more fingerprints here...
}

# Simulated vote database
vote_database = {
    # Voter ID: Vote
}

def register_voter(voter_id, fingerprint):
    """
    Registers a new voter in the fingerprint database.
    """
    # Hash the fingerprint
    fingerprint_hash = hashlib.sha256(fingerprint.encode()).hexdigest()
    
    # Store the fingerprint hash in the database
    fingerprint_database[voter_id] = fingerprint_hash
    
    print(f"Voter {voter_id} registered successfully!")

def vote(voter_id, vote):
    """
    Records a vote from a registered voter.
    """
    # Check if the voter is registered
    if voter_id not in fingerprint_database:
        print("Voter is not registered!")
        return
    
    # Verify the fingerprint
    fingerprint = input("Scan your fingerprint: ")  # Simulated fingerprint scanning
    
    fingerprint_hash = hashlib.sha256(fingerprint.encode()).hexdigest()
    
    if fingerprint_hash != fingerprint_database[voter_id]:
        print("Fingerprint verification failed!")
        return
    
    # Record the vote
    vote_database[voter_id] = vote
    
    print(f"Vote recorded successfully for voter {voter_id}!")

def get_vote_result():
    """
    Retrieves the vote result.
    """
    # Count the votes
    vote_count = {}
    
    for vote in vote_database.values():
        if vote in vote_count:
            vote_count[vote] += 1
        else:
            vote_count[vote] = 1
    
    # Print the vote result
    print("Vote Result:")
    for candidate, count in vote_count.items():
        print(f"{candidate}: {count} votes")

# Example usage:
register_voter("voter1", "fingerprint_data1")
register_voter("voter2", "fingerprint_data2")

vote("voter1", "Candidate A")
vote("voter2", "Candidate B")
vote("voter1", "Candidate B")

get_vote_result()


# In[ ]:




