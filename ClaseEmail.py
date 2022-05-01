import re


class Email:
    #Atributos
    __idCuenta = ''
    __dominio = ''
    __tipoDom = ''
    __password = ''

    #Metodos
    def __init__(self):
        self.__idCuenta = ''
        self.__dominio = ''
        self.__tipoDom = ''
        self.__password = ''
    
    def retornaEmail(self):
        return '{}@{}.{}'.format(self.__idCuenta,self.__dominio,self.__tipoDom)
    
    def getDominio(self):
        return self.__dominio
    
    def crearCuenta(self,correo,passw=''):
        #Validar correo
        if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',correo.lower()):
            #Divido elementos
            i = correo.find('@')
            j = correo[i:].find('.')
            
            self.__idCuenta = correo[:i]
            self.__dominio = correo[i+1:i+j]
            self.__tipoDom = correo[i+j+1:]

            print('Su correo es: {}'.format(self.retornaEmail()))
            if passw == '':
                print('Configure su password: ')
                self.__setPass()
            else:
                self.__password = passw
            print ("La cuenta se creo con exito!")
            return False #No hubo error retorno false
        else:
            print ("Correo electronico incorrecto, reintente.")
            return True #Hubo un error retorno true

    def __setPass(self):
        passw = input('Ingrese password: ')
        passw2 = input('Reingrese password: ')
        while(passw != passw2):
            print('Las password no coincide, reinente.')
            passw = input('Ingrese password: ')
            passw2 = input('Reingrese password: ')
        print('Password configurada con exito!')
        self.__password = passw

    def changePass(self):
        oldPass = input('Ingrese su password actual FIN para salir: ')
        while(oldPass != self.__password and oldPass.lower() != 'fin'):
            print('Su password es incorrecta.')
            oldPass = input('Ingrese su password actual o FIN para salir: ')
        if(oldPass.lower() != 'fin'):
            print('Configure su nueva password: ')
            self.__setPass()
            