distance_in_cm=float(input("Enter distance in centimeter:"))
distance_in_km=distance_in_cm/(10**5)
distance_in_feet=(distance_in_cm/100)*3.28
distance_in_inches=distance_in_cm/2.54

print("Distance in:")
print("KM:\t{}\nFeet:\t{}\nInches:\t{}".format(distance_in_km,distance_in_feet,distance_in_inches))
