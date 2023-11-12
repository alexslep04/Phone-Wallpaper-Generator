import configparser
valueset = configparser.ConfigParser()
valueset.read('values.ini')
apikey = valueset.get('DEFAULT', 'api')
print(apikey)
