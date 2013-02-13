import hashlib

# Shard list with partitions
# Each value is the upper limit of the shard, including the value itself
# values are written in hex with lowercase letters
shards = [  '0a000000000000000000000000000000',
            '40000000000000000000000000000000',
            '80000000000000000000000000000000',
            'c0000000000000000000000000000000',
            ]

#
# Calculate on which shard the user 
#
def getShard(username):
    # receive username and calculate the hash
    hash = hashlib.md5(username).hexdigest()

    print "hash\t= %s" % hash # debug
    
    n = 0
    while(True):
        # try to fit in shard n range
        if(hash <= shards[n]):
            return n #exit the function, returning the shard number
        # if not, go to next
        else:
            n = n + 1
            #if is the last shard
            if(n == len(shards)):
                return n #exit the function, returning the shard number

#                
#main script to test the function
#

# usernames for test
usernames = [   'fgh45658',
                'luigi',
                'Luciana',
                'mario',
                'someuser',
                'test'
                ]

for username in usernames:
    print "user\t= %s" % username # debug
    print "shard#\t= %s\n" % getShard(username)
    
