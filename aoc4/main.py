def exercise2(Passports):
    valid = 0
    for passport in Passports:
        info = dict(x.split(":") for x in passport.split())
        if "byr" in info and 1920 <= int(info["byr"]) and int(info["byr"]) <= 2002:
            if "iyr" in info and 2010 <= int(info["iyr"]) and int(info["iyr"]) <= 2020:
                if "eyr" in info and 2020 <= int(info["eyr"]) and int(info["eyr"]) <= 2030:
                    if "ecl" in info and info["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                        if "pid" in info and len(info["pid"]) == 9:
                            if "hcl" in info and info["hcl"][:1] == '#':
                                if "hgt" in info and "cm" in info["hgt"]:
                                    if (info["hgt"][:1] == '1') and (150 <= int(info["hgt"][:3])) and (int(info["hgt"][:3]) <= 193):
                                        valid = valid + 1
                                elif "hgt" in info and "in" in info["hgt"]:
                                    if (59 <= int(info["hgt"][:2])) and (int(info["hgt"][:2]) <= 76):
                                        valid = valid + 1
    return(valid)

def exercise1(Passports):
    valid = 0
    for passport in Passports:
        info = passport.split()
        if len(info) == 8 or (len(info) == 7 and "cid" not in passport):
            valid = valid + 1
    return(valid)

#### Main ####
Passports = open('input', 'r').read().split("\n\n")
print("There are", len(Passports), "passports total.")
print("Valid passports exercise 1:", exercise1(Passports))
print("Valid passports exercise 2:", exercise2(Passports))