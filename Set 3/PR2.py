data=input("Enter main string:")
find_str=input("Enter string to find in main string:")
index=data.find(find_str)
if index!=-1:
    result=data[index:len(data)]
    print("\n\nExtracted String: ",result)
else: print("\n\nNo match found.")
