# metadata
print("Script for batch submission of genome files (.gbk/.embl) \nDate: 3/17/2021\nJakub Krulik, Athabasca University\nLast Modified: 3/26/2021\n")

import requests, sys
from requests_toolbelt.multipart.encoder import MultipartEncoder
server = "http://www.pathogenomics.sfu.ca/islandviewer"
ext = "/rest/submit/"


# asks user if they would like to use their email address
emailQ = str(input("Do you want to use your email? (Y/N):"))
if emailQ == "Y":
    email = str(input("input email address:"))
elif emailQ == "N":
    email = 'my@email.address.com'


# input number of files to be processed
n = int(input("Number of files to be processed:"))
n = n - 1


# asks for the input of all files to be submitted for analysis
i = 0
filePath = []
while i <= n:
    filePath.append(input("Drag .gbk/.embl file " + str(i + 1) + " into the command line: "))
    i = i + 1


# final check with user before submission of files
i = 0
while i <= n:
    print(str(filePath[i]))
    i = i + 1
    
j = False
while j <= False:
  submit = str(input("Submit files? (Y/N, if N, you will exit the program):"))
  if submit == "N":
    exit()
    j = True
  elif submit == "Y":
    print("Your files are being submitted, no more prompts will follow")
    j = True
  else:
    print("please ensure you answer with Y or N")
    j = False


# file submission loop
i = 0
while i <= n:
    mygenome = filePath[i]

    # checks the file extension of the file
    fileExtension = ".gbk"

    # ensures that the correct file extension is specified for each file, and submits files
    if fileExtension in mygenome:
        extn = 'GENBANK'
    else:
        extn = 'EMBL'


    multipart_data = MultipartEncoder(
        fields={ "format_type": extn,
                    'email_addr': email,
    #  For incomplete genomes include a reference accession
    #             'ref_accnum': 'NC_022792.1',
                    'genome_file': ('filename', open(mygenome, 'rb'), 'text/plain')}
    )
    headers={'Content-Type': multipart_data.content_type,
                'x-authtoken': 'fbf55d36-ee4a-dc69-4cf8-db045cbd4b66'}

    r = requests.post(server+ext, headers=headers, data=multipart_data)

    if not r.ok:
        r.raise_for_status()
        sys.exit()

    decoded = r.json()
    print(repr(decoded))
    i = i + 1
    mygenome = None
