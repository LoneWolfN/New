import pickle 
def datechk():
    u=int(input("enter the date (DD)-"))
    k=1
    j=int(input("enter the month (MM)-"))
    y=int(input("enter the year (YYYY)-"))
    while k==1:
        if j<0 or j>12:
            print("incorrect month")
            j=int(input("enter the correct month"))
        else:
            k=0
            m=j
    l=1
    list1=[1,3,5,7,8,10,12]
    list2=[4,6,9,11]
    while l==1:
        if m in list1:
            if u<1 or u>31:
                print("incorrect date")
                u=int(input("enter the correct date"))
            else:
                l=0
                d=u
        elif m in list2:
            if u<1 or u>30:
                print("incorrect date")
                u=int(input("enter the correct date"))
            else:
                l=0
                d=u
        elif m==2:
            if y%4==0:
                if u<0 or u>29:
                    print("incorrect date")
                else:
                    l=0
                    d=u
            else:
                if u<0 or u>28:
                    print("incorrect date")
                    u=int(input("enter the correct date"))
                else:
                    l=0
                    d=u
    p=str(y)
    while len(p)!=4 or y>2020 or y<2015:
        print("incorrect year")
        y=int(input("enter the year"))
        p=str(y)
    da=[d,m,y]
    daa=""
    c=1
    for i in da:
        if c==1:
            daa+=str(i)+"-"
        elif c==2:
            daa+=str(i)+"-"
        elif c==3:
            daa+=str(i)
        c+=1    
    return(daa)
def facilitychk():
    ch=1
    c=0
    while ch!=0:
        print("choose your facility from the options given below:")
        f=open("Facilityfile.DAT","rb")
        d=0
        try:
            while True:
                fac=pickle.load(f)
                d+=1
                facs=str(fac)
                facsl=facs.split(',')
                c=1
                for i in facsl:
                    if c==1:
                        S=str(i)
                    elif c==2:
                        fa=str(i)
                    c+=1
                print(S,":",fa)
        except:
            f.close()
        print("[0 : if u dont want another facility]")
        ch1=int(input("enter the number of the 1st facility u want-"))
        ch2=int(input("enter the number of the 2nd facility u want-"))
        ch3=int(input("enter the number of the 3rd facility u want-"))
        if ch1==ch2 or ch2==ch3 or ch3==ch1:
            print("wrong entry, cannot have more than one facility")
            ch1=int(input("enter the number of the 1st facility u want-"))
            ch2=int(input("enter the number of the 2nd facility u want-"))
            ch3=int(input("enter the number of the 3rd facility u want-"))
        elif ch1>d or ch2>d or ch3>d:
            print("wrong entry, only",d,"choices available")
            ch1=int(input("enter the number of the 1st facility u want-"))
            ch2=int(input("enter the number of the 2nd facility u want-"))
            ch3=int(input("enter the number of the 3rd facility u want-"))
        ch=0
        
    h=[ch1,ch2,ch3]
    hs=""
    c=1
    for i in h:
        if c==1:
            hs+=str(i)+","
        elif c==2:
            hs+=str(i)+","
        elif c==3:
            hs+=str(i)
    return(hs)
def phonechk():
    ph=int(input("enter the phone number-"))
    k=0
    while k==0:
        phs=str(ph)
        if len(phs)<8 or len(phs)>8:
            print("incorrect number")
            ph=int(input("enter the phone number-"))
        else:
            k=1
            ph=int(phs)
    return(ph)
