def insert(hash_table, key, value):
    hash_key = hash(key) % len(hash_table)
    key_exists = False
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            key_exists = True
            break
    if key_exists:
        bucket[i] = ((key, value))
    else:
        bucket.append((key, value))

hash_table = [[] for _ in range(10)]
insert(hash_table, 9, 'Japan')
insert(hash_table, 22, 'UAE')
insert(hash_table, 18, 'Russia')
print(hash_table)
