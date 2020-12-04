valid = 0
Passports = open('input', 'r').read().split("\n\n")
print(len(Passports))
for passport in Passports:
    info = dict(x.split(":") for x in passport.split())
    if "byr" in info and 1920 <= int(info["byr"]) and int(info["byr"]) <= 2002:
        if "iyr" in info and 2010 <= int(info["iyr"]) and int(info["iyr"]) <= 2020:
            if "eyr" in info and 2020 <= int(info["eyr"]) and int(info["eyr"]) <= 2030:
                if "ecl" in info and info["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                    if "pid" in info and len(info["pid"]) == 9:
                        if "hcl" in info and info["hcl"][:1] == '#':
                            print(info["hcl"])
                            if "hgt" in info and "cm" in info["hgt"]:
                                if (info["hgt"][:1] == '1') and (150 <= int(info["hgt"][:3])) and (int(info["hgt"][:3]) <= 193):
                                    valid = valid + 1
                            elif "hgt" in info and "in" in info["hgt"]:
                                if (59 <= int(info["hgt"][:2])) and (int(info["hgt"][:2]) <= 76):
                                    valid = valid + 1
print(valid)






    #if (len(info) == 8) or ("cid" not in passport and len(info) == 7):






    #print(passport)
    #info = passport.split()
    #print(info)
    #print(len(info))
    #if len(info) < 8:
        #if "cid" in passport or len(info) < 7:
            #print("INVALID:")
            #print(passport)
        #else:
            #valid = valid + 1
            #print("VALID:")
            #print(passport)
    #else:
        #valid = valid + 1
        #print("VALID:")
        #print(passport)




#byr (Birth Year) - four digits; at least 1920 and at most 2002.
#iyr (Issue Year) - four digits; at least 2010 and at most 2020.
#eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
#hgt (Height) - a number followed by either cm or in:
#If cm, the number must be at least 150 and at most 193.
#If in, the number must be at least 59 and at most 76.
#hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
#ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
#pid (Passport ID) - a nine-digit number, including leading zeroes.
#cid (Country ID) - ignored, missing or not.
