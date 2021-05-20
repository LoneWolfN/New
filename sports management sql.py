from datetime import date,timedelta
import mysql.connector as ms
x=0
while x==0:
    n=str(input("enter your password-"))
    mys=ms.connect(host='localhost',user='root',passwd="{0}".format(n))
    cur=mys.cursor(buffered=True)
    if mys.is_connected():
        print("Connected")
        x=1
    else:
        print("not connected")
f='use sports'
cur.execute(f)
def feesfilecrad():
    f='drop table if exists feesfile'
    cur.execute(f)
    f='create table feesfile(NO numeric(2),FEES numeric(5),DATE date)'
    cur.execute(f)
    mys.commit()
    f='select * from member'
    cur.execute(f)
    data=cur.fetchall()
    for i in data:
        s1=i[5]
        s2=i[6]
        s3=i[7]
        bl=[]
        bl+=[s1]
        bl+=[s2]
        bl+=[s3]
        a=10000
        for v in bl:
            if v==0:
                a+=0
            else:
                a+=2000
        n=i[0]
        chd=i[4]
        diff=timedelta(days=365)
        dat=chd+diff
        g='insert into feesfile values({0},{1},"{2}")'.format(n,a,dat)
        cur.execute(g)
        mys.commit()
    k='select * from feesfile'
    cur.execute(k)
    data=cur.fetchall()
    for i in data:
        print(i)
def facilityfilecr():
    f='drop table if exists facfile'
    cur.execute(f)
    f='create table facfile(NO numeric(2),FAC char(20))'
    cur.execute(f)
    n1=1
    f1='football'
    f='insert into facfile values({0},"{1}")'.format(n1,f1)
    cur.execute(f)
    f='select * from facfile'
    cur.execute(f)
    mys.commit()
def memberfilecr():
    f='drop table if exists member'
    cur.execute(f)
    f='create table member(CODE numeric(2),NAME char(30),PH numeric(8),AD char(50),D date,H1 numeric(2),H2 numeric(2),H3 numeric(2))'
    cur.execute(f)
    mys.commit()
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
    da=[y,m,d]
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
    while ch!=0:
        print("choose your facility from the options given below:")
        f='select * from facfile'
        cur.execute(f)
        facsl=cur.fetchall()
        d=0
        for i in facsl:
            d+=1
            S=str(i[0])
            fa=str(i[1])
            print(S,":",fa)
        print("0 : if u dont want another facility]")
        ch1=int(input("enter the number of the 1st facility u want-"))
        ch2=int(input("enter the number of the 2nd facility u want-"))
        ch3=int(input("enter the number of the 3rd facility u want-"))
        s=0
        while(s==0):
            if (ch1==ch2 or ch2==ch3 or ch3==ch1) and (ch1!=0 and ch2!=0 and ch3!=0):
                print("wrong entry, cannot have more than one facility of the same type")
                ch1=int(input("enter the number of the 1st facility u want-"))
                ch2=int(input("enter the number of the 2nd facility u want-"))
                ch3=int(input("enter the number of the 3rd facility u want-"))
            elif ch1>d or ch2>d or ch3>d:
                print("wrong entry, only",d,"choices available")
                ch1=int(input("enter the number of the 1st facility u want-"))
                ch2=int(input("enter the number of the 2nd facility u want-"))
                ch3=int(input("enter the number of the 3rd facility u want-"))
            else:
                s=1
                ch=0
    h=[ch1,ch2,ch3]
    return(h)
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
def tablecr():
    f='desc member'
    cur.execute(f)
    data=cur.fetchall()
    for i in data:
        print(i)
def memberfilead(n):
    c=0
    f='select * from member'
    cur.execute(f)
    data=cur.fetchall()
    for i in data:
        c+=1
        while c==i[0]:
            c+=1
    
    for k in range(n):
        n=str(input("enter the name-"))
        d=datechk()
        ph=phonechk()
        ad=str(input("enter the full address"))
        h=facilitychk()
        s1=h[0]
        s2=h[1]
        s3=h[2]
        f='insert into member values({0},"{1}",{2},"{3}","{4}",{5},{6},{7})'.format(c,n,ph,ad,d,s1,s2,s3)
        cur.execute(f)
        mys.commit()

def display():
    print("+==================================================================================================================+")
    print("|  ID   |      NAME       |  NUMBER  |                     ADDRESS                        |    DATE    |CH1|CH2|CH3|")
    print("+------------------------------------------------------------------------------------------------------------------+")
    f='select * from member'
    cur.execute(f)
    data=cur.fetchall()
    for i in data:
        ID=str(i[0])
        a=ID
        if len(ID)<5:
            n=5-len(ID)
            ID=""
            for h in range(n):
                ID+=" "
            ID+=a
        name=str(i[1])
        a=name
        if len(name)<15:
            n=15-len(name)
        name=""
        for h in range(n):
            name+=" "
        name+=a
        ph=str(i[2])
        ad=str(i[3])
        a=ad
        if len(ad)<50:
            n=50-len(ad)
            ad=""
            for h in range(n):
                 ad+=" "
            ad+=a
        d=str(i[4])
        if i[5]=="0":
            ch1="-"
        else:
            ch1=str(i[5])
        if i[6]=="0":
            ch2="-"
        else:
            ch2=str(i[6])
        if i[7]=="0":
            ch3="-"
        else:
            ch3=str(i[7])
        print("|",ID,"|",name,"|",ph,"|",ad,"|",d,"|",ch1,"|",ch2,"|",ch3,"|")
        print("+------------------------------------------------------------------------------------------------------------------+")
def facilityfilead(n):
    for i in range(n):
        g=str(input('Enter the facility to be entered-'))
        f='select * from facfile'
        cur.execute(f)
        data=cur.fetchall()
        c=1
        for i in data:
            c+=1
        while c==i[0]:
            c+=1
        f='insert into facfile values({0},"{1}")'.format(c,g)
        cur.execute(f)
        mys.commit()
def facilityd():
    print("+======================+")
    print("|SNO|     FACILITY     |")
    f='select * from facfile'
    cur.execute(f)
    facsl=cur.fetchall()
    for i in facsl:
        print("+----------------------+")
        S=str(i[0])
        fa=str(i[1])
        fac=""
        if len(fa)<16 or len(fa)==16:
            a=16-len(fa)
            for i in range(a):
                fac+=" "
        fac+=fa
        print("|",S,"|",fac,"|")
    print("+======================+")
def facilitydel():
    print("deleting")
    facilityd()
    ch=1
    while ch!=0:
        print("1.search on the basis of number")
        print("2.search on the basis of name")
        print("3.display changes")
        print("0.continue")
        ch=int(input("enter your choice-"))
        if ch==1:
            f='select * from facfile'
            cur.execute(f)
            n=int(input("enter the number of facility to be deleted-"))
            data=cur.fetchall()
            for i in data:
                if n==i[0]:
                    f='delete from facfile where NO={0}'.format(n)
                    cur.execute(f)
                    mys.commit()
        elif ch==2:
            f='select * from facfile'
            cur.execute(f)
            n=str(input("enter the name of facility to be deleted-"))
            data=cur.fetchall()
            for i in data:
                if n==i[1]:
                    f='delete from facfile where FAC="{0}"'.format(n)
                    cur.execute(f)
                    mys.commit()
        elif ch==3:
            facilityd()
        elif ch==0:
            ch=0
def recordmodif():
    ch=1
    display()
    while ch!=0:
        print("1.search on the basis of code")
        print("2.search on the basis of name")
        print("3.search on the basis of phone number")
        print("4.display changes")
        print("0.continue")
        ch=int(input("enter your choice-"))
        if ch==1:
            n=int(input("enter the code to be searched-"))
            f='select * from member where CODE={0}'.format(n)
            cur.execute(f)
            data=cur.fetchall()
            for i in data:
                print(i)
            for i in range(1):
                print("1.change name")
                print("2.change date")
                print("3.change address")
                print("4.change phone number")
                print("5.change facilities")
                ch=int(input("enter your choice 1/2/3/4/5/0-"))
                if ch==1:
                    na=str(input("enter the new name"))
                    f='update member set NAME="{0}" where CODE={1}'.format(na,n)
                    cur.execute(f)
                    mys.commit()
                elif ch==2:
                    da=datechk()
                    f='update member set D="{0}" where CODE={1}'.format(da,n)
                    cur.execute(f)
                    mys.commit()
                elif ch==3:
                    ad=str(input("enter the new address"))
                    f='update member set AD="{0}" where CODE={1}'.format(ad,n)
                    cur.execute(f)
                    mys.commit()
                elif ch==4:
                    ph=int(input("enter new phone number"))
                    f='update member set PH={0} where CODE={1}'.format(ph,n)
                    cur.execute(f)
                    mys.commit()
                elif ch==5:
                    h=facilitychk()
                    s1=h[0]
                    s2=h[1]
                    s3=h[2]
                    f='update member set H1={0} where CODE={1}'.format(s1,n)
                    cur.execute(f)
                    f='update member set H2={0} where CODE={1}'.format(s2,n)
                    cur.execute(f)
                    f='update member set H3={0} where CODE={1}'.format(s3,n)
                    cur.execute(f)
                    feesfilecrad()
                    mys.commit()
                
                elif ch==0:
                    ch=0
        elif ch==2:
            n=str(input("enter the name to be searched-"))
            f='select * from member where NAME="{0}"'.format(n)
            cur.execute(f)
            data=cur.fetchall()
            for i in data:
                print(i)
            for i in range(1):
                print("1.change name")
                print("2.change date")
                print("3.change address")
                print("4.change phone number")
                print("5.change facilities")
                ch=int(input("enter your choice 1/2/3/4/5/0-"))
                if ch==1:
                    na=str(input("enter the new name"))
                    f='update member set NAME="{0}" where NAME="{1}"'.format(na,n)
                    cur.execute(f)
                    mys.commit()
                elif ch==2:
                    da=datechk()
                    f='update member set D="{0}" where NAME="{1}"'.format(da,n)
                    cur.execute(f)
                    mys.commit()
                elif ch==3:
                    ad=str(input("enter the new address"))
                    f='update member set AD="{0}" where NAME="{1}"'.format(ad,n)
                    cur.execute(f)
                    mys.commit()
                elif ch==4:
                    ph=int(input("enter new phone number"))
                    f='update member set PH={0} where NAME="{1}"'.format(ph,n)
                    cur.execute(f)
                    mys.commit()
                elif ch==5:
                    h=facilitychk()
                    s1=h[0]
                    s2=h[1]
                    s3=h[2]
                    f='update member set H1={0} where NAME="{1}"'.format(s1,n)
                    cur.execute(f)
                    f='update member set H2={0} where NAME="{1}"'.format(s2,n)
                    cur.execute(f)
                    f='update member set H1={0} where NAME="{1}"'.format(s3,n)
                    cur.execute(f)
                    feesfilecrad()
                    mys.commit()
                
                elif ch==0:
                    ch=0
        elif ch==3:
            n=int(input("enter the name to be searched-"))
            f='select * from member where PH={0}'.format(n)
            cur.execute(f)
            data=cur.fetchall()
            for i in data:
                print(i)
            for i in range(1):
                print("1.change name")
                print("2.change date")
                print("3.change address")
                print("4.change phone number")
                print("5.change facilities")
                ch=int(input("enter your choice 1/2/3/4/5/0-"))
                if ch==1:
                    na=str(input("enter the new name"))
                    f='update member set NAME="{0}" where PH={1}'.format(na,n)
                    cur.execute(f)
                    mys.commit()
                elif ch==2:
                    da=datechk()
                    f='update member set D="{0}" where PH={1}'.format(da,n)
                    cur.execute(f)
                    mys.commit()
                elif ch==3:
                    ad=str(input("enter the new address"))
                    f='update member set AD="{0}" where PH={1}'.format(ad,n)
                    cur.execute(f)
                    mys.commit()
                elif ch==4:
                    ph=int(input("enter new phone number"))
                    f='update member set PH={0} where PH={1}'.format(ph,n)
                    cur.execute(f)
                    mys.commit()
                elif ch==5:
                    h=facilitychk()
                    s1=h[0]
                    s2=h[1]
                    s3=h[2]
                    f='update member set H1={0} where PH={1}'.format(s1,n)
                    cur.execute(f)
                    f='update member set H2={0} where PH={1}'.format(s2,n)
                    cur.execute(f)
                    f='update member set H1={0} where PH={1}'.format(s3,n)
                    cur.execute(f)
                    feesfilecrad()
                    mys.commit()
                
                elif ch==0:
                    ch=0
            
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
        print("4.display all members")
        print("0.continue")
        ch=int(input("enter your choice-"))
        if ch==1:
            n=int(input("enter the code to be searched-"))
            f='select * from member where CODE={0}'.format(n)
            cur.execute(f)
            data=cur.fetchall()
            for i in data:
                print('+---------------------------------------------------------------+')
                print("|",i[0],"|",i[1],"|",i[2],"|",i[3],"|",i[4],"|",i[5],"|",i[6],"|",i[7],"|")
                print('+---------------------------------------------------------------+')

        if ch==2:
            n=str(input("enter the name to be searched-"))
            f='select * from member where NAME="{0}"'.format(n)
            cur.execute(f)
            data=cur.fetchall()
            for i in data:
                print('+---------------------------------------------------------------+')
                print("|",i[0],"|",i[1],"|",i[2],"|",i[3],"|",i[4],"|",i[5],"|",i[6],"|",i[7],"|")
                print('+---------------------------------------------------------------+')
        if ch==3:
            n=int(input("enter the phone number to be searched-"))
            f='select * from member where PH={0}'.format(n)
            cur.execute(f)
            data=cur.fetchall()
            for i in data:
                print('+---------------------------------------------------------------+')
                print("|",i[0],"|",i[1],"|",i[2],"|",i[3],"|",i[4],"|",i[5],"|",i[6],"|",i[7],"|")
                print('+---------------------------------------------------------------+')
            
        if ch==4:
            display()
def delrec():
    print()
    print("---------------------------------DELETING----------------------------------")
    print()
    ch=1
    while ch!=0:
        print("1.search on the basis of code")
        print("2.search on the basis of name")
        print("3.search on the basis of phone number")
        print("4.display changes")
        print("0.continue")
        ch=int(input("enter your choice-"))
        display()
        if ch==1:
            f='select * from member'
            cur.execute(f)
            n=int(input("enter the code of person to be deleted-"))
            data=cur.fetchall()
            for i in data:
                if i[0]==n:
                    f='select * from member where CODE={0}'.format(n)
                    cur.execute(f)
                    j=cur.fetchall()
                    for i in j:
                        print()
                        print("|",i[0],"|",i[1],"|",i[2],"|",i[3],"|",i[4],"|",i[5],"|",i[6],"|",i[7],"|-has been deleted")
                        print()
                    f='delete from member where CODE={0}'.format(n)
                    cur.execute(f)
                    feesfilecrad()
                    mys.commit()
                else:
                    print("record not found")
        elif ch==2:
            f='select * from member'
            cur.execute(f)
            n=str(input("enter the name of person to be deleted-"))
            data=cur.fetchall()
            for i in data:
                if i[1]==n:
                    f='select * from member where NAME="{0}"'.format(n)
                    cur.execute(f)
                    j=cur.fetchall()
                    for i in j:
                        print("|",i[0],"|",i[1],"|",i[2],"|",i[3],"|",i[4],"|",i[5],"|",i[6],"|",i[7],"|  has been deleted")
                    f='delete from member where NAME="{0}"'.format(n)
                    cur.execute(f)
                    feesfilecrad()
                    mys.commit()
                else:
                    print("record not found")
        elif ch==3:
            f='select * from member'
            cur.execute(f)
            n=int(input("enter the phone number of person to be deleted-"))
            data=cur.fetchall()
            for i in data:
                if i[2]==n:
                    f='select * from member where PH={0}'.format(n)
                    cur.execute(f)
                    j=cur.fetchall()
                    for i in j:
                        print("|",i[0],"|",i[1],"|",i[2],"|",i[3],"|",i[4],"|",i[5],"|",i[6],"|",i[7],"|  has been deleted")
                    f='delete from member where PH={0}'.format(n)
                    cur.execute(f)
                    feesfilecrad()
                    mys.commit()
                else:
                    print("record not found")
        elif ch==4:
            display()
        elif ch==0:
            ch=0

def feesd():
    f='select * from feesfile'
    cur.execute(f)
    data=cur.fetchall()
    print("+===========================================+")
    print("|Sno.|   Date Paid   |  Amount |  Next Date |")
    print("+-------------------------------------------+")

    for i in data:
        l=i[0]
        a=str(i[1])
        aa=""
        if len(a)<7:
            n=7-len(a)
            for s in range(n):
                aa+=" "
        aa+=a
        datet=(i[2])
        d=str(i[2])
        da=""
        if len(d)<13:
            n=13-len(d)
            for s in range(n):
                da+=" "
        da+=d
        diff=timedelta(days=365)
        dat=datet+diff
        print("| ",l,"|",da,"|",aa,"|",dat,"|")
        print("+-------------------------------------------+")
ch=1
while ch!=0:
    print("enter choice")
    print('10.HAS TO BE RUN ONCE IF THE CODE HAS NOT BEEN RUN ON DEVICE BEFORE')
    print("1.Member file")
    print("2.Facility file")
    print("3.Fees file")
    print("0.Close")
    ch=int(input("enter your choice: 0/1/2/3"))
    if ch==10:
        print("New databse sports has been created, along with a new table member and facfile")
        memberfilecr()
        facilityfilecr()
        print("only to be run once on a new device")
    elif ch==1:
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
                memberfilead(n)
                feesfilecrad()
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
                n=int(input("enter the number of facilities to be added-"))
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
                feesd()

