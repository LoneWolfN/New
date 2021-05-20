from os import remove, rename
import pickle
from datetime import date,timedelta
    
def feesfilead():
    f=open("Feesfile.DAT","wb")
    p=open("Memberfile.DAT","rb")
    try:
        while True:
            i=pickle.load(p)
            s=[]
            b=i[5]
            bs=b.split(',')
            bl=[]
            for k in range(0,3):
                bl+=[int(bs[k])]
            a=10000
            for v in bl:
                if v==0:
                    a+=0
                else:
                    a+=2000
            s+=[i[0]]
            n=i[4]
            j=n.split('-')
            d=int(j[0])
            m=int(j[1])
            y=int(j[2])
            chd=date(y,m,d)
            diff=timedelta(days=365)
            dat=chd+diff
            s+=[[d,m,y]]
            s+=[dat]
            s+=[a]
            pickle.dump(s,f)
            print(s)
    except:
        f.close()
        p.close()    
    
def feesd():
    f=open("Feesfile.DAT","rb")
    print("+===========================================+")
    print("|Sno.|   Date Paid   |  Amount |  Next Date |")
    try:
        while True:
            i=pickle.load(f)
            print("|-------------------------------------------|")
            c=0
            for k in range(4):
                if c==0:
                    S=i[0]
                elif c==1:
                    d=str(i[1])
                    da=""
                    if len(d)<13:
                        n=13-len(d)
                        for l in range(n):
                            da+=" "
                    da+=d
                elif c==2:
                    dan=i[2]
                elif c==3:
                    am=i[3]
                c+=1
            print("|",S,"|",da,"| ",am," |",dan,"|")
            
    except:
        print("+===========================================+")
        f.close()
                   
    
def facilityfilecr():
    f=open("Facilityfile.DAT","wb")
    s=[1,"tennis"]
    p=[2,"badminton"]
    d=[3,"football"]
    pickle.dump(s,f)
    pickle.dump(p,f)
    pickle.dump(d,f)
    f.close()
facilityfilecr()
def facilityfilead(n):
    for i in range(n):
        f=open("Facilityfile.DAT","rb")
        c=1
        try:
            while True:
                i=pickle.load(f)
                c+=1
        except:
            f.close()
    
        f=open("Facilityfile.DAT","ab")
        n=str(input("enter the name-"))
        s=[c,n]
        pickle.dump(s,f)
        f.close()
def facilityd():
    with open("Facilityfile.DAT","rb") as f:
        try:
            while True:
                fac=pickle.load(f)
                facs=str(fac)
                print("+-------------------+")
                facsl=facs.split(',')
                c=1
                for i in facsl:
                    if c==1:
                        S=str(i)
                    elif c==2:
                        fa=str(i)
                        fac=""
                        if len(fa)<16 or len(fa)==16:
                            a=16-len(fa)
                            for i in range(a):
                                fac+=" "
                        fac+=fa
                            
                    c+=1
                print(S,"|",fac)
        except:
            f.close()
    print("+-------------------+")
def facilitydel():
    print("deleting")
    facilityd()
    ch=1
    f=open("Facilityfile.DAT","rb")
    while ch!=0:
        print("1.search on the basis of number")
        print("2.search on the basis of name")
        print("4.display changes")
        print("0.continue")
        ch=int(input("enter your choice-"))
        if ch==1:
            n=int(input("enter the number of facility to be deleted-"))
            f=open("Facilityfile.DAT","rb")
            ft=open("temp.DAT","wb")
            try:
                while True:
                    k=pickle.load(f)
                    if k[0]!=n:
                        pickle.dump(k,ft)
            except:
                f.close()
                ft.close()
            remove("Facilityfile.DAT")
            rename("temp.dat","Facilityfile.DAT")
        elif ch==2:
            n=str(input("enter the name of facility to be deleted-"))
            f=open("Facilityfile.DAT","rb")
            ft=open("temp.DAT","wb")
            try:
                while True:
                    k=pickle.load(f)
                    if k[1]!=n:
                        pickle.dump(k,ft)
            except:
                f.close()
                ft.close()
            remove("Facilityfile.DAT")
            rename("temp.dat","Facilityfile.DAT")
        elif ch==4:
            facilityd()
        elif ch==0:
            ch=0
def memberfilecr(n):
    c=0
    for i in range(n):
        f=open("Memberfile.DAT","wb")
        c=c+1
        n=str(input("enter the name-"))
        from myfile import datechk,facilitychk,phonechk
        d=datechk()
        ph=phonechk()
        ad=str(input("enter the full address"))
        h=facilitychk()
        s=[c,n,ph,ad,d,h]
        pickle.dump(s,f)
        f.close()

def memberfileadd(n):
    for i in range(n):
        f=open("Memberfile.DAT","rb")
        c=0
        try:
            while True:
                i=pickle.load(f)
                c+=1
        except:
            f.close()
        n=str(input("enter the name-"))
        from myfile import datechk,facilitychk,phonechk
        o=0
        m=str(c)+n[o]
        f=open("Memberfile.DAT","rb")
        try:
            while True:
                i=pickle.load(f)
                if i[0]==m:
                    o+=1
                
        except:
            m=str(c)+n[o]
            f.close()
        f=open("Memberfile.DAT","ab")
        d=datechk()
        ph=phonechk()
        ad=str(input("enter the full address seperated by '-' -"))
        h=facilitychk()
        s=[m,n,ph,ad,d,h]
        pickle.dump(s,f)
        f.close()

def display():
    print("+=====================================================================================================================+")
    print("|  ID |      NAME       |   NUMBER  |                     ADDRESS                        |     DATE     |  CH1|CH2|CH3|")
    with open("Memberfile.DAT","rb") as f:
        try:
            while True:
                rec=pickle.load(f)
                recs=str(rec)
                print("+---------------------------------------------------------------------------------------------------------------------+")
                recsl=recs.split(',')
                c=1
                for i in recsl:
                    if c==1:
                        ID=str(i)
                        a=ID
                        if len(ID)<5:
                            n=5-len(ID)
                            ID=""
                            for i in range(n):
                                ID+=" "
                            ID+=a
                    elif c==2:
                        name=i
                        a=name
                        if len(name)<15:
                            n=15-len(name)
                            name=""
                            for i in range(n):
                                name+=" "
                            name+=a
                    elif c==3:
                        ph=str(i)
                    elif c==4:
                        ad=str(i)
                        a=ad
                        if len(ad)<50:
                            n=50-len(ad)
                            ad=""
                            for i in range(n):
                                ad+=" "
                            ad+=a
                    elif c==5:
                        d=str(i)
                    elif c==6:
                        if i=="0":
                            ch1="-"
                        else:
                            ch1=str(i)
                    elif c==7:
                        if i=="0":
                            ch2="-"
                        else:
                            ch2=str(i)
                    elif c==8:
                        if i=="0":
                            ch3="-"
                        else:
                            ch3=str(i)
                    
                    c+=1
                print(ID,"|",name,"|",ph,"|",ad,"|",d,"|",ch1,"|",ch2,"|",ch3,"|")
                    
        except:
            f.close()
    print("+=====================================================================================================================+")
def recordmodif():
    ch=1
    f=open("Memberfile.DAT","rb")
    display()
    while ch!=0:
        print("1.search on the basis of code")
        print("2.search on the basis of name")
        print("3.search on the basis of phone number")
        print("4.display changes")
        print("0.continue")
        ch=int(input("enter your choice-"))
        if ch==1:
            n=input("enter the code to be searched-")
            f=open("Memberfile.DAT","rb")
            ft=open("temp.DAT","wb")
            l=0
            p=0
            try:
                while True:
                    k=pickle.load(f)
                    l+=1
            except:
                f.close()
            f=open("Memberfile.DAT","rb")
            try:
                while True:
                    k=pickle.load(f)
                    if k[0]==n:
                        print(k)
                        for i in range(1):
                            print("1.change name")
                            print("2.change date")
                            print("3.change address")
                            print("4.change phone number")
                            print("5.change facilities")
                            ch=int(input("enter your choice 1/2/3/4/5/0-"))
                            if ch==1:
                                na=str(input("enter the new name"))
                                k[1]=na
                                print(k[1])
                                pickle.dump(k,ft)
                            elif ch==2:
                                from myfile import datechk
                                k[4]=datechk()
                                pickle.dump(k,ft)
                            elif ch==3:
                                ad=str(input("enter the new address"))
                                k[3]=ad
                                pickle.dump(k,ft)
                                
                            elif ch==4:
                                ph=int(input("enter new phone number"))
                                k[2]=ph
                                pickle.dump(ph,ft)
                            elif ch==5:
                                from myfile import facilitychk
                                h=facilitychk()
                                k[5]=h
                                pickle.dump(k,ft)
                                
                    else:
                        p+=1
                        pickle.dump(k,ft)
            
            except:
                if p==l:
                    print("code not found")
                f.close()
                ft.close()
            remove("Memberfile.DAT")
            rename("temp.DAT","Memberfile.DAT")
        elif ch==2:
            n=str(input("enter the name to be searched-"))
            f=open("Memberfile.DAT","rb")
            ft=open("temp.DAT","wb")
            l=0
            p=0
            try:
                while True:
                    k=pickle.load(f)
                    l+=1
            except:
                f.close()
            f=open("Memberfile.DAT","rb")
            try:
                while True:
                    k=pickle.load(f)
                    if k[1]==n:
                        print(k)
                        for i in range(1):
                            print("1.change name")
                            print("2.change date")
                            print("3.change address")
                            print("4.change phone number")
                            print("5.change facilities")
                            ch=int(input("enter your choice 1/2/3/4/5/0-"))
                            if ch==1:
                                na=str(input("enter the new name"))
                                k[1]=na
                                print(k[1])
                                print(k)
                                pickle.dump(k,ft)
                                print("here")
                            elif ch==2:
                                from myfile import datechk
                                k[4]=datechk()
                                pickle.dump(k,ft)
                            elif ch==3:
                                ad=str(input("enter the new address"))
                                k[3]=ad
                                pickle.dump(k,ft)
                                
                            elif ch==4:
                                ph=int(input("enter new phone number"))
                                k[2]=ph
                                pickle.dump(k,ft)
                            elif ch==5:
                                from myfile import facilitychk
                                h=facilitychk()
                                k[5]=h
                                pickle.dump(k,ft)
                    
                    else:
                        p+=1
                        pickle.dump(k,ft)
            except:
                print("here")
                if p==l:
                    print("name not found")
                f.close()
                ft.close()
            remove("Memberfile.DAT")
            rename("temp.DAT","Memberfile.DAT")
            
        elif ch==3:
            n=int(input("enter the phone number to be searched-"))
            f=open("Memberfile.DAT","rb")
            ft=open("temp.DAT","wb")
            l=0
            p=0
            try:
                while True:
                    k=pickle.load(f)
                    l+=1
            except:
                f.close()
            f=open("Memberfile.DAT","rb")
            try:
                while True:
                    k=pickle.load(f)
                    if k[2]==n:
                        print(k)
                        for i in range(1):
                            print("1.change name")
                            print("2.change date")
                            print("3.change address")
                            print("4.change phone number")
                            print("5.change facilities")
                            ch=int(input("enter your choice 1/2/3/4/5/0-"))
                            if ch==1:
                                na=str(input("enter the new name"))
                                k[1]=na
                                print(k[1])
                                
                                pickle.dump(k,ft)
                            elif ch==2:
                                from myfile import datechk
                                k[4]=datechk()
                                pickle.dump(k,ft)
                            elif ch==3:
                                ad=str(input("enter the new address"))
                                k[3]=ad
                                pickle.dump(k,ft)
                                
                            elif ch==4:
                                ph=int(input("enter new phone number"))
                                k[2]=ph
                                pickle.dump(k,ft)
                            elif ch==5:
                                from myfile import facilitychk
                                h=facilitychk()
                                k[5]=h
                                pickle.dump(k,ft)
                                
                    else:
                        p+=1
                        pickle.dump(k,ft)
            
            except:
                if p==l:
                    print("address not found")
                f.close()
                ft.close()
            remove("Memberfile.DAT")
            rename("temp.DAT","Memberfile.DAT")
            
            
            
        elif ch==4:
            display()
        else:
            ch=0
def membersrch():
    ch=1
    while ch!=0:
        print("1.search on the basis of code")
        print("2.search on the basis of name")
        print("3.search on the basis of phone number")
        print("4.display changes")
        print("0.continue")
        ch=int(input("enter your choice-"))
        if ch==1:
            n=input("enter the code to be searched-")
            f=open("Memberfile.DAT","rb")
            l=0
            p=0
            try:
                while True:
                    k=pickle.load(f)
                    l+=1
            except:
                f.close()
            f=open("Memberfile.DAT","rb")
            try:
                while True:
                    k=pickle.load(f)
                    if k[0]==n:
                        print("+----------------------------------------------------+")
                        print(k[0],"|",k[1],"|",k[2],"|",k[3],"|",k[4],"|",k[5],"|")
                        print("+----------------------------------------------------+")
                    else:
                        p+=1
            
            except:
                if p==l:
                    print("code not found")
                else:
                    continue
                f.close()
        if ch==2:
            n=str(input("enter the name to be searched-"))
            f=open("Memberfile.DAT","rb")
            l=0
            p=0
            try:
                while True:
                    k=pickle.load(f)
                    l+=1
            except:
                f.close()
            f=open("Memberfile.DAT","rb")
            try:
                while True:
                    k=pickle.load(f)
                    if k[1]==n:
                        print("+----------------------------------------------------+")
                        print(k[0],"|",k[1],"|",k[2],"|",k[3],"|",k[4],"|",k[5],"|")
                        print("+----------------------------------------------------+")
                    else:
                        p+=1
            
            except:
                if p==l:
                    print("name not found")
                else:
                    continue
                f.close()
        if ch==3:
            n=int(input("enter the phone number to be searched-"))
            f=open("Memberfile.DAT","rb")
            l=0
            p=0
            try:
                while True:
                    k=pickle.load(f)
                    l+=1
            except:
                f.close()
            f=open("Memberfile.DAT","rb")
            try:
                while True:
                    k=pickle.load(f)
                    if k[2]==n:
                        print("+----------------------------------------------------+")
                        print(k[0],"|",k[1],"|",k[2],"|",k[3],"|",k[4],"|",k[5],"|")
                        print("+----------------------------------------------------+")
                    else:
                        p+=1
            
            except:
                if p==l:
                    print("number not found")
                else:
                    continue
                f.close()
        if ch==4:
            display()
def delrec():
    print("deleting")
    ch=1
    while ch!=0:
        print("1.search on the basis of code")
        print("2.search on the basis of name")
        print("3.search on the basis of phone number")
        print("4.display changes")
        print("0.continue")
        ch=int(input("enter your choice-"))
        if ch==1:
            n=input("enter the code of person to be deleted-")
            f=open("Memberfile.DAT","rb")
            ft=open("temp.DAT","wb")
            ff=open("Feesfile.DAT","rb")
            fn=open("temp2.DAT","wb")
            try:
                while True:
                    k=pickle.load(f)
                    l=pickle.load(ff)
                    print("l=",l[0])
                    if k[0]!=n:
                        pickle.dump(k,ft)
                    if l[0]!=n:
                        pickle.dump(l,fn)
            except:
                f.close()
                ft.close()
                ff.close()
                fn.close()
            remove("Memberfile.DAT")
            rename("temp.dat","Memberfile.DAT")
            remove("Feesfile.DAT")
            rename("temp2.DAT","Feesfile.dat")
        elif ch==2:
            n=str(input("enter the name of person to be deleted-"))
            f=open("Memberfile.DAT","rb")
            ft=open("temp.DAT","wb")
            ff=open("Feesfile.DAT","rb")
            fn=open("temp2.DAT","wb")
            j=""
            try:
                while True:
                    k=pickle.load(f)
                    l=pickle.load(ff)
                    if k[1]!=n:
                        j=k[0]
                        pickle.dump(k,ft)
                    if l[0]==j:
                        pickle.dump(l,fn)
                    
            except:
                f.close()
                ft.close()
                ff.close()
                fn.close()
            remove("Memberfile.DAT")
            rename("temp.dat","Memberfile.DAT")
            remove("Feesfile.DAT")
            rename("temp2.DAT","Feesfile.dat")
        elif ch==3:
            n=int(input("enter the phone number of person to be deleted-"))
            f=open("Memberfile.DAT","rb")
            ft=open("temp.DAT","wb")
            ff=open("Feesfile.DAT","rb")
            fn=open("temp2.DAT","wb")
            j=""
            try:
                while True:
                    k=pickle.load(f)
                    l=pickle.load(ff)
                    if k[2]!=n:
                        j=k[0]
                        pickle.dump(k,ft)
                    if l[0]==j:
                        pickle.dump(l,fn)
                    
            except:
                f.close()
                ft.close()
                ff.close()
                fn.close()
            remove("Memberfile.DAT")
            rename("temp.dat","Memberfile.DAT")
            remove("Feesfile.DAT")
            rename("temp2.DAT","Feesfile.dat")
        elif ch==4:
            display()
        ch=0
    
        
                        
facilityfilecr()                        
ch=1
while ch!=0:
    print("enter choice")
    print("1.Member file")
    print("2.Facility file")
    print("3.Fees file")
    print("0.Close")
    ch=int(input("enter your choice: 0/1/2/3"))
    if ch==1:
        h=1
        while h!=0:
            print("Enter choice")
            print("1.Add a new member")
            print("2.Search for member")
            print("3.Modify a member")
            print("4.Delete a member")
            print("5.Display member table")
            print("0.Close")
            h=int(input("enter your choice:0/1/2/3/4"))
            if h==1:
                n=int(input("enter the number of members to be added-"))
                memberfileadd(n)
                feesfilead()
            elif h==2:
                membersrch()
            elif h==3:
                recordmodif()
            elif h==4:
                delrec()
            elif h==5:
                display()
            elif h==0:
                h=0
    elif ch==2:
        h=1
        while h!=0:
            print("Enter choice")
            print("1.Add new facilities")
            print("2.Display facility table")
            print("3.Delete a facility")
            print("0.Close")
            h=int(input("enter your choice:0/1/2/3"))
            if h==1:
                n=int(input("enter the number of members to be added-"))
                facilityfilead(n)
            elif h==2:
                facilityd()
            elif h==3:
                facilitydel()
            elif h==0:
                h=0
    elif ch==3:
        h=1
        while h!=0:
            print("1.Display fees table")
            print("0.Close")
            h=int(input("enter your choice:0/1"))
            if h==1:
                feesfilead()
                feesd()

            


    
    
    
