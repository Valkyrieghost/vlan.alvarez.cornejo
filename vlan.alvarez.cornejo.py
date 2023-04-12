vlan = input("Ingrese un N° de VLAN: ")
name = input("Ingrese el name: ")
interface1 = input("Ingrese la interfaz de acceso: ")
interface2 = input("Ingrese el puerto troncal: ")



print("\nvlan",vlan)
print("name",name)



print("\ninterface",interface1)
print("switchport mode acces")
print("Switchport acces vlan",vlan)
print("Description °°°Pc", name , "°°°")
print("Duplex full")
print("Speed 100")
print("Spanning-tree portfast")

print("\ninterface",interface2)
print("Switchport trunk allowed vlan add",vlan)

print("\nPara validar la informacion ejecute lo siguiente")

print("\nshow interface trunk")
print("Show vlan")
print("Show  interfaces ",interface1 ,"switchport")