import argparse
import urllib.parse
import urllib.request

def read_mail_addresses(filename):
    '''
    Read the mail address file and return the mail address list.
    If there is any non-ASCII character, reading may fail.
    '''
    mail_addresses = []
    with open(filename, 'r') as file:
        mail_addresses = [line.strip() for line in file]
    return mail_addresses

def registrate(mail):
    '''
    Registrate the mail and return whether it succeeded or not.
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
    mail_addresses_filename     the filename of the file containing mail addresses.
    '''
    print('===================================================================')
    print('  THE IDOLM@STER MILLION LIVE! THEATER DAYS Preregistration Tool   ')
    print('===================================================================')

    # Read mail addresses.
    mail_addresses = read_mail_addresses(mail_addresses_filename)
    print('Read ' + mail_addresses_filename + '.')

    # Registrate one by one.
    print('Start registrating each mail address:')
    successCount = 0
    for mail_address in mail_addresses:
        print('  ' + mail_address + '  ' + '.' * (50 - len(mail_address)), end='')
        if registrate(mail_address):
            print('succeeded')
            successCount += 1
        else:
            print('failed')

    # Show the overall result.
    print('\nSuccessfully registrate ' + str(successCount) + ' out of ' + str(len(mail_addresses)) + ' mail addresses! Keep going!')

if __name__ == '__main__':
    # Parse the inputs.
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', default='mail_addresses.txt',
        help='set the file containing the mail addresses. The default filename is \'mail_addresses.txt\'.')
    args = parser.parse_args()
    if args.input:
        mail_addresses_filename = args.input

    main(mail_addresses_filename)