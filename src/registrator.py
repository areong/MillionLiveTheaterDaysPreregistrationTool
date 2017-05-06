import argparse
import urllib.parse
import urllib.request

def read_mail_addresses(filename):
    '''
    Read the mail address file and return the mail address list.
    Do not check the address format. Just read all lines.
    '''
    mail_addresses = []
    read_successfully = True
    with open(filename, 'r') as file:
        try:
            mail_addresses = [line.strip() for line in file]
        except UnicodeDecodeError:
            print('There are invalid characters in ' + filename + '.')
            print('It is recommended to use ASCII charactors only.')
            read_successfully = False
    return mail_addresses, read_successfully

def registrate(mail):
    '''
    Registrate the mail to the official site.
    Return whether it registrated successfully.
    '''
    url = 'https://prereg.bn-ent.net/common/serial.php'
    values = {
        'action' : 'sendmail',
        'app' : 'imasml_theater',
        'device_type' : '2',
        'mailAddr' : mail,
        'comMail' : ''
        }
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    request = urllib.request.Request(url, data)
    registrate_successfully = False
    with urllib.request.urlopen(request) as response:
        # Read the lines.
        # If 'form' exists, the mail address is already registrated.
        # Else, registrate successfully.
        registrate_successfully = True
        for line in response.readlines():
            if 'form' in line.decode('utf-8'):
                registrate_successfully = False
                break
    return registrate_successfully

def main(mail_addresses_filename):
    '''
    Input:
    mail_addresses_filename     the filename of the file containing the mail addresses.
    '''
    print('===================================================================')
    print('  THE IDOLM@STER MILLION LIVE! THEATER DAYS Preregistration Tool   ')
    print('===================================================================')

    # Read mail addresses.
    mail_addresses, read_successfully = read_mail_addresses(mail_addresses_filename)
    if not read_successfully:
        return 0
    print('There are ' + str(len(mail_addresses)) + ' mail addresses in ' + mail_addresses_filename + '.')

    # Registrate one by one.
    print('Start registrating each mail address:')
    mail_addresses_count = 1
    success_count = 0
    for mail_address in mail_addresses:
        print(str(mail_addresses_count) + '. ' + mail_address + '  ' + '.' * (55 - len(str(mail_addresses_count)) - len(mail_address)), end='')
        if registrate(mail_address):
            print('succeeded')
            success_count += 1
        else:
            print('failed')
        mail_addresses_count += 1

    # Show the overall result.
    print('\nSuccessfully registrate ' + str(success_count) + ' out of ' + str(len(mail_addresses)) + ' mail addresses! Keep going!')

if __name__ == '__main__':
    # Parse the inputs.
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', default='mail_addresses.txt',
        help='set the file which contains the mail addresses. The default filename is \'mail_addresses.txt\'.')
    args = parser.parse_args()
    if args.input:
        mail_addresses_filename = args.input

    main(mail_addresses_filename)

    input('Press enter to terminate...')