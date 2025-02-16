# p. 23
# dictionaries
# dictionary key/value can contain any data type
# can access by get method or square brackets
print("\ndictionaries")
spanish_english = {
    "uno": "one",
    "dos": "two",
    "tres": "three",
    1: "one"
}
print(spanish_english)

# # get value by key
# print(spanish_english.get("dos"))
# print(spanish_english[1])
# # add elements to a dictionary using square brackets (no add function)
# spanish_english["quatro"] = "four"
# print(spanish_english)

# #iterate over dictionary keys using for .. in
# print("\nIterate over dictionary w/ for .. in")
# for key in spanish_english:
#     print(f"{key} means {spanish_english[key]}")

# #.values contains all values
# print("\n.values() to return all key-value pairs")
# for value in spanish_english.values():
#     print(f"{value}", end=" ")

# #get both keys and values using .items()
# print(".items() returns both key and value")
# for k, v in spanish_english.items():
#     print(f"k, v: {k}, {v}")

# #does key exist in dictionary?
# print("check key existence...")
# if "uno" in spanish_english:
#     print("Yes, 'uno' is in dictionary")

# #use pop(key) to remove item or popitem() to remove last item
# #pop returns removed value, popitem() returns entire item (k,v)
# print("\npop and popitem to remove items")
# print(spanish_english)
# # pop returns value of item deleted
# item_1 = spanish_english.pop(1)
# print(f"item_1={item_1}")
# print(spanish_english)
# # popitem returns entire item (k, v)
# item_2 = spanish_english.popitem()
# print(f"item_2={item_2}")
# print(spanish_english)
