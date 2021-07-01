class tool:
    def __init__(self):
        print("""
    ----------------------------------------
    [            NGDOX RECOVER             ]
    ----------------------------------------
    |    1 > START RECOVER                 |
    |    2 > SETTINGS                      |
    |    3 > EXIT                          |
    ---------------------------------------""" )

    def Recover(self):
        import os,time
        if os.path.isdir('/sdcard/recoveredimages')==False:
            os.system('mkdir recoveredimages')

        
        List=os.listdir('/sdcard/DCIM/.thumbnails')
        print('total Files (',len(List),')')
        print('recovery starta in 3 seconds ...')
        time.sleep(3)

        n=1
        for i in List:
            os.system(f'cp /sdcard/DCIM/.thumbnails/{i} /sdcard/recoveredimages')
            print('[',n,']',i,'\033[0;32;40mrecovered ...\033[0;37;40m')
            n+=1
        return True

if __name__=='__main__':
    tool()
    choice=input(' > ')
    if choice=='1':
        if tool().Recover() == True:
            print('All files recovered sucessfully !')
    else:
        exit()