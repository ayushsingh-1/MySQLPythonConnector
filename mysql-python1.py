#Hello

import mysql.connector;

conn=mysql.connector.connect(user='root', password='password', host='127.0.0.1',database='mock_staff')
cursor=conn.cursor()
cursor.execute('select database()')
data=cursor.fetchone()
print('Connection established to ',data,'\n')
print()

def queries():

    #Choose Country region
    print("\nChoose the Country Region: \n")

    q1='select * from company_regions'
    cursor.execute(q1)
    results=cursor.fetchall()

    j=1
    for i in results:
        print(j,i[1],",",i[2])
        j+=1
        print('\n')

    region=input("Enter a Serial Number")

    q2='select company_regions, country from company_regions where region_id=%s'
    cursor.execute(q2,(region,))
    results=cursor.fetchall()
    for i in results:
        print("\nRegion chosen : ",i[0],",",i[1])


    #Choose Department of Employees
    print("\nChoose the Department of Employee: \n")

    q3='select department from company_divisions'
    cursor.execute(q3)
    results=cursor.fetchall()

    j=1
    for i in results:
        print(j,i[0])
        j+=1
        print('\n')

    a=input("Type the Department Name: ")
    dept=str(a)
    print("Department Chosen: ",dept)


    # #Choose Department of Employees
    # print("Choose the Department of Employee: \n")

    # q3='select department from company_divisions'
    # cursor.execute(q3)
    # results=cursor.fetchall()

    # j=1
    # for i in results:
    #     print(j,i[0])
    #     j+=1
    #     print('\n')

    # a=input("Select a serial number")
    # a=int(a)

    # dept=results[a-1]
    # print(type(dept))
    # dept=str(dept)
    # print("Department Chosen: ",dept)


    # for i in results:
    #     print(i[a-1])


    # q2='select department, company_divisions from company_divisions where region_id=%s'
    # cursor.execute(q2,(a,))
    # results=cursor.fetchall()
    # for i in results:
    #     print("\nRegion chosen : ",i[0],",",i[1])

    #Display Employees 

    print("\n--------------------Staff Menu--------------------\n")
    print("1. Display all records (No search criteria)")
    print("2. Display filtered records (Apply a search criteria) \n")

    emp_ch=input("Enter your choice (1/2)")

    #Display all records (No search criteria)
    if emp_ch=='1':
        q4='select s.id, s.last_name, s.email, s.gender ,cd.department ,s.start_date ,s.salary ,s.job_title ,cr.company_regions, cr.country from staff as s join company_divisions as cd on cd.department=s.department join company_regions as cr on cr.region_id=s.region_id where cd.department = %s and cr.region_id = %s'
        cursor.execute(q4,(dept,region,))
        results=cursor.fetchall()

        print("--------------------Records Retrieved--------------------\n")
        print("\nNo. of rows retrieved: ",len(results))
        for i in results:
            print('\n')
            print('ID: ',i[0])
            print("Last Name: ",i[1])
            print("Email: ",i[2])
            print('Gender: ',i[3])
            print('Department: ',i[4])
            print('Start Date: ',i[5])
            print('Salary ',i[6])
            print('Job Title: ',i[7])
            print('Region: ',i[8])
            print('Country: ',i[9])
            print('\n')

    #Display all records (Apply a search criteria)
    elif emp_ch=='2':
        print("--------------------Search Criteria Menu--------------------\n")
        print("1. Search by Last Name")
        print("2. Search by Email")
        print("3. Search by Job Title")
        print("4. Search by Last Name and Email")

        sc_ch=input("Enter your choice (1/2/3/4)")
        
        if sc_ch=='1':
                print("--------------------Search by Last Name--------------------\n")
                name=input("\nEnter the Last Name")
                print("\nLast Name Entered: ",name)
                q5='select s.id, s.last_name, s.email, s.gender ,cd.department ,s.start_date ,s.salary ,s.job_title ,cr.company_regions, cr.country from staff as s join company_divisions as cd on cd.department=s.department join company_regions as cr on cr.region_id=s.region_id where cd.department = %s and cr.region_id = %s and s.last_name like %s'
                cursor.execute(q5,(dept,region,"%" +name+ "%",))
                results=cursor.fetchall()

                print("--------------------Records Retrieved--------------------\n")
                print("\nNo. of rows retrieved: ",len(results),"\n")
                for i in results:
                    print('\n')
                    print('ID: ',i[0])
                    print("Last Name: ",i[1])
                    print("Email: ",i[2])
                    print('Gender: ',i[3])
                    print('Department: ',i[4])
                    print('Start Date: ',i[5])
                    print('Salary ',i[6])
                    print('Job Title: ',i[7])
                    print('Region: ',i[8])
                    print('Country: ',i[9])
                    print('\n')
        elif sc_ch=='2':
                print("--------------------Search by Email--------------------\n")
                email=input("\nEnter the Email")
                print("\nEmail Entered: ",email)
                q6='select s.id, s.last_name, s.email, s.gender ,cd.department ,s.start_date ,s.salary ,s.job_title ,cr.company_regions, cr.country from staff as s join company_divisions as cd on cd.department=s.department join company_regions as cr on cr.region_id=s.region_id where cd.department = %s and cr.region_id = %s and s.email like %s'
                cursor.execute(q6,(dept,region,"%" +email+ "%",))
                results=cursor.fetchall()

                print("--------------------Records Retrieved--------------------\n")
                print("\nNo. of rows retrieved: ",len(results),"\n")
                for i in results:
                    print('\n')
                    print('ID: ',i[0])
                    print("Last Name: ",i[1])
                    print("Email: ",i[2])
                    print('Gender: ',i[3])
                    print('Department: ',i[4])
                    print('Start Date: ',i[5])
                    print('Salary ',i[6])
                    print('Job Title: ',i[7])
                    print('Region: ',i[8])
                    print('Country: ',i[9])
                    print('\n')
        elif sc_ch=='3':
                print("--------------------Search by Job Title--------------------\n")
                job_t=input("\nEnter the Job Title")
                print("\nJob Title Entered: ",job_t)
                q7='select s.id, s.last_name, s.email, s.gender ,cd.department ,s.start_date ,s.salary ,s.job_title ,cr.company_regions, cr.country from staff as s join company_divisions as cd on cd.department=s.department join company_regions as cr on cr.region_id=s.region_id where cd.department = %s and cr.region_id = %s and s.job_title like %s'
                cursor.execute(q7,(dept,region,"%" +job_t+ "%",))
                results=cursor.fetchall()

                print("\nNo. of rows retrieved: ",len(results),"\n")

                print("--------------------Records Retrieved--------------------\n")
                for i in results:
                    print('\n')
                    print('ID: ',i[0])
                    print("Last Name: ",i[1])
                    print("Email: ",i[2])
                    print('Gender: ',i[3])
                    print('Department: ',i[4])
                    print('Start Date: ',i[5])
                    print('Salary ',i[6])
                    print('Job Title: ',i[7])
                    print('Region: ',i[8])
                    print('Country: ',i[9])
                    print('\n')
        elif sc_ch=='4':
                print("\n--------------------Search by Last Name and Email--------------------\n")
                name=input("\nEnter the Last Name")
                print("\nLast Name Entered: ",name)
                email=input("\nEnter the Email")
                print("\nEmail Entered: ",email)
                q8='select s.id, s.last_name, s.email, s.gender ,cd.department ,s.start_date ,s.salary ,s.job_title ,cr.company_regions, cr.country from staff as s join company_divisions as cd on cd.department=s.department join company_regions as cr on cr.region_id=s.region_id where cd.department = %s and cr.region_id = %s and s.last_name like %s and s.email like %s'
                cursor.execute(q8,(dept,region,"%" +name+ "%","%" +email+ "%",))
                results=cursor.fetchall()

                print("\nNo. of rows retrieved: ",len(results),"\n")

                print("--------------------Records Retrieved--------------------\n")
                for i in results:
                    print('\n')
                    print('ID: ',i[0])
                    print("Last Name: ",i[1])
                    print("Email: ",i[2])
                    print('Gender: ',i[3])
                    print('Department: ',i[4])
                    print('Start Date: ',i[5])
                    print('Salary ',i[6])
                    print('Job Title: ',i[7])
                    print('Region: ',i[8])
                    print('Country: ',i[9])
                    print('\n')


def recurse():
    print("Do you wish to continue (y/n): ")
    ch=input("Do you wish to continue (y/n)")
    if ch=='y':
        queries()
        recurse()
    elif ch=='n':
        conn.close()
        print('\nThanks for wasting your valuable time on us!')

queries()
recurse()
