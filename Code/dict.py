class entry:
    def __init__(self, key, value, next = None):
        self.key = key
        self.value = value
        self.next = next
        
# Dictionary (key-value pairs) using a hash function (i.e. Gives key an index for a list)
class dict:
    # size = number of buckets
    # length = number of key-value pairs in dict
    # scale = length / size (Should always be <= 2)
    # data = A list of entries of key-value pairs
    def __init__(self):
        self.size = 32
        self.length = 0
        self.scale = self.length / self.size
        self.data = [None] * self.size

    # Takes a key-value pair and either:
    # - If key doesn't exist, add key-value pair (grow the size of list if needed to keep scale <= 2)
    # - If key exist, replace value
    def add_entry(self, key, value):
        if (self.get_value(key) is None):
            self.length += 1
            self.scale = self.length / self.size
            self.check_grow()
            pos = hash(key) % self.size
            self.data[pos] = entry(key, value, self.data[pos])
        else:
            pos = hash(key) % self.size
            bucket = self.data[pos]
            while (bucket is not None):
                if (bucket.key == key):
                    bucket.value = value
                else:
                    bucket = bucket.next

    # Takes a key and return its value if exist, None if not exist
    def get_value(self, key):
        pos = hash(key) % self.size
        bucket = self.data[pos]
        while (bucket is not None):
            if (bucket.key == key):
                return bucket.value
            else:
                bucket = bucket.next
        return None
    
    # If scale > 2, grow the size of the list and put each key-value pair in new position
    def check_grow(self):
        if (self.scale > 2):
            self.size = self.size * 2
            new_data = [None] * self.size
            for bucket in self.data:
                cur_bucket = bucket
                while (cur_bucket is not None):
                    pos = hash(cur_bucket.key) % self.size
                    new_data[pos] = entry(cur_bucket.key, cur_bucket.value, new_data[pos])
                    cur_bucket = cur_bucket.next
            self.data = new_data
            self.scale = self.length / self.size
            
    # Prints the contents of the dict
    def get_data(self):
        temp = ""
        index = 0
        for bucket in self.data:
            bucket_str = ""
            cur_bucket = bucket
            while (cur_bucket is not None):
                bucket_str = bucket_str + str(cur_bucket.key) + "," + str(cur_bucket.value) + " -> "
                cur_bucket = cur_bucket.next
            bucket_str = str(index) + ": " + bucket_str + "None"
            temp = temp + "\n" + bucket_str
            index += 1
        print("***")
        print(temp[1:])
        print("***")
    
vec = dict()





