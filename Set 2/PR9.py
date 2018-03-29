name = input('Enter name to view relation: ')
name = name.lower()

if name=='ann' or name == 'marty':
    print("""
    parent of Bill, Cathy and Frank in Family 1.
    Grandparent of Madd, Sally and Sarah.
    """)
elif name == 'bill':
    print("""
    Child of Ann and Marty.
    Sibling of Cathy and Frank.
    """)
elif name == 'cathy':
    print("""
    Child of Ann and Marty.
    Sibling of Bill and Frank.
    Parent of Madd and Sally.
    """)
elif name == 'frank':
    print("""
    Child of Ann and Marty.
    Sibling of Cathy and Bill.
    Parent of Sarah.
    """)
elif name == 'don':
    print("""
    Parent of Madd and Sally.
    """)
elif name == 'madd':
    print("""
    Child of Cathy and Don.
    Grandchild of Ann and Marty.
    Sibling of Sally.
    """)
elif name == 'sally':
    print("""
    Child of Cathy and Don.
    Grandchild of Ann and Marty.
    Sibling of Madd.
    """)
elif name == 'jill':
    print("""
    Parent of Sarah.
    Child of Debbie and Phil.
    """)
elif name == 'sarah':
    print("""
    Child of Frank and Jill.
    Grandchild of Ann and Marty.
    """)
elif name == 'debbie':
    print("""
    Parent of Jill and Betty.
    Grandparent of Sarah.
    """)
elif name == 'phil':
    print("""
    Parent of Jill and Betty.
    Grandparent of Sarah.
    """)
elif name == 'betty':
    print("""
    Parent of Mary, Jane and Bart.
    Child of Debbie and Phil.
    """)
elif name == 'paul':
    print("""
    Parent of Mary, Jane and Bart.
    """)
elif name == 'mary':
    print("""
    Grandchild of Debbie and Phil.
    Child of Betty and Paul.
    Sibling of Jane and Bart.
    """)
elif name == 'jane':
    print("""
    Grandchild of Debbie and Phil.
    Child of Betty and Paul.
    Sibling of Mary and Bart.
    """)
elif name == 'bart':
    print("""
    Grandchild of Debbie and Phil.
    Child of Betty and Paul.
    Sibling of Jane and Mary.
    """)