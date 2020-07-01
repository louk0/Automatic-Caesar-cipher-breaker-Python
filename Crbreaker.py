L='ABCDEFGHIJKLMNOPQESTUVWXYZ'
#sinartisi kwdikopoihshs
def ceasar_encrypt(ini,steps):
    n=len(ini)
    ini_output=''
    for i in range(n):
        character=ini[i]                        
        location=L.find(character)
        new_location=(location+steps)%26
        ini_output+=L[new_location]   
    return ini_output
#sinartisi apodikopoihshs
def ceasar_derypt(ini,steps):
    n=len(ini)
    ini_output=''
    for i in range(n):
        character=ini[i]
        location=L.find(character)
        new_location=(location-steps)%26
        ini_output+=L[new_location]
    return ini_output




W=input('Welcome! insert one of the choices 1)Codification 2)Decoding 3)Exit  ')
while W=='2' or W=='1':
    if W=='2':
        insert=input('insert text for decoding  ')
        key=int(input('insert the key for decoding  '))
        F=ceasar_derypt(insert,key)
        print ('The coded text:',insert,',translate it into:',F)
    
    elif W=='1':
        insert=input('insert text for codification ')
        key=int(input('insert the key for the codification '))
        F=ceasar_encrypt(insert,key)
        print ('The text:',insert,',coded into:',F)
    
    W=input('Insert one of the choices 1)Codification 2)Decoding 3)Exit ')

print ('goodbye')
