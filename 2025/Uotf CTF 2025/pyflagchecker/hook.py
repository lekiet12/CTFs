import marshal

original_loads = marshal.loads

def hook_marshal(data):
    print(f"Data: {data}")
    return original_loads(data)

marshal.loads = hook_marshal

# save in folder site-packages