print("Hello World")
print(type(3))
print(type(2019))
ballots = 1,341
print(ballots)
print(type(ballots))
print(type(73.81))
print(type("Hello World"))
print(type(True))

print(5 + 2 * 3)
print(8 // 5 - 3)
print(8 + 22 * 2 - 4)
print(16 - 3 / 2 + 7 - 1)
print(3 ** 3 % 5)
print(5 + 9 * 3 / 2 - 4)
print((5 + 2) * 3)
print((8 // 5) - 3)
print(8 + (22 * (2 - 4)))
print(16 - 3 / (2 + 7) - 1)
print(3 ** (3 % 5))
print(5 + ( 9* 3 / 2 - 4))
print(5 + (9 * 3 / (2 - 4)))

counties = ["Arapahoe","Denver","Jefferson"]
print(counties)
print(counties[0])
print(counties[2])
print(counties[-1])
print(counties[-2])
print(len(counties))
print(counties[0:2])
print(counties[0:1])
print(counties[:2])
print(counties[1:])
print(counties.append("El Paso"))
print(counties)
print(counties.insert(2, "El Paso"))
print(counties)
print(counties.remove("El Paso"))
print(counties)
print(counties.pop(3))
print(counties)
counties[2] = "El Paso"
print(counties)

counties_tuple = ("Arapahoe","Denver","Jefferson")
print(len(counties_tuple))
print(counties_tuple[1])

counties_dict = {}
counties_dict["Arapahoe"] = 422829
print(counties_dict)
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
print(counties_dict)
print(len(counties_dict))
print(counties_dict.items())
print(counties_dict.keys())
print(counties_dict.values())
print(counties_dict.get("Denver"))
print(counties_dict["Arapahoe"])

voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
print(voting_data)