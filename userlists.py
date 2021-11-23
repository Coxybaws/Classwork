#Network Lists
def  printusers():
    for i in range(len(users)):
        print(users[i] + ',' + ips[i] + ',' + networks[i] + ',' + gateways[i] + ',' + devices[i] + ',' + models[i])


users = ['Thomas', 'Gearaldine']
ips = ['192.186.48.22','192.168.48.44']
networks = ['192.168.48.00/24','192.168.48.00/24']
gateways = ['192.168.48.1','192.168.48.1']
devices = ['Dell', 'HP']
models =['Optiplex 5050','PC 7900']


newUser = input('Enter a new user:')
users.append(newUser)
newIP = input('Enter ip address:')
ips.append(newIP)
newNetwork = input('Enter network address:')
networks.append(newNetwork)
newGateway = input('Enter gateway address:')
gateways.append(newGateway)
newDevices = input('Enter new device make:')
devices.append(newDevices)
newModels = input('Enter device model:')
models.append(newModels)
