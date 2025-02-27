import xmlrpc.client


url ="http://localhost:8012/" # Url of the target machine
db = "mydb" #Database name
username = 'admin' # username
password = "admin" #password
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url)) # connecting the model with the python script

def check_uid():
    """
    Description : Checking the user id
    """
    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    uid=common.authenticate(db,username,password,{})
    return uid

uid=check_uid() #Calling the function to get the user id

def fetch_patients_name():
    """
    Fetch the data from the patients model
    """
    data=models.execute_kw(db, uid, password, 'patients.description', 'name_search', []) # Fetching the data from the model
    print(data)

def count_name():
    """
    Description : Count the number of occurence of the particular records
    """
    print(models.execute_kw(db, uid, password, 'patients.description', 'search_count', [[['name', '=','Dev' ]]])) # Seacch count the data with the condition

def fetch_full_data():
    """
    Description: Fetching the full description of the the patient data
    """
    id=models.execute_kw(db, uid, password, 'patients.description', 'search_read', [[]], {'fields': [], 'limit': 1})
    print(id[0]['id'])

def delete_info():
    """
    Description: Deleting the record of a particular id if exists
    """
    email_address="Enter the email address you want to delete the record"
    id=models.execute_kw(db, uid, password, 'patients.description', 'search_read', [[["email_address","=",email_address]]], {'fields': ['id'], 'limit': 1})
    try:
        models.execute_kw(db, uid, password, 'patients.description', 'unlink', [[id[0]['id']]])
        print("Data Successfully deleted\nUpdated Records After Deletion\n")
        print(models.execute_kw(db, uid, password, 'patients.description', 'name_search', []))
    except Exception as e:
        print(f"{e} exception ocuurs")

def update_info(name,email_address,mobile_number,date_of_birth):
    """
    Description: Update the records by fetching the id using email address if alreadyh exists
    """
    try:
        id=models.execute_kw(db, uid, password, 'patients.description', 'search_read', [[["email_address","=",email_address]]], {'fields': ['id'], 'limit': 1})

        # models.execute_kw(db, uid, password, 'patients.description', 'create', [[5], {'name': "Newer partner","mobile_number":"8761875974","email_address":"email@gmail.com","date_of_birth":"2025-01-01"}])
        models.execute_kw(db, uid, password, 'patients.description', 'write', [[id[0]['id']], {'name': name,"mobile_number":mobile_number,"email_address":email_address,"date_of_birth":date_of_birth}])
        print(f"Data Updated Successfully link with the {email_address}")
        print(models.execute_kw(db, uid, password, 'patients.description', 'name_search', []))
    except Exception as e:
        print(f"{e} exception ocuurs")

def create_new_record():
    """
    Description: Creating the new record in the patient information model
    """
    name=input("Enter The Name")
    email_address=input("Enter the email address")
    mobile_number=input("Enter the mobile number")
    date_of_birth=input("Enter the date of birth YYYY-MM-DD")
    already_exists = models.execute_kw(db, uid, password, 'patients.description', 'search_read', [[["email_address","=",email_address]]], {'fields': ['id'], 'limit': 1})
    if already_exists:
        update_info(name,email_address,mobile_number,date_of_birth)
    else:
        try:
            models.execute_kw(db, uid, password, 'patients.description', 'create', [[], {"name": name,"mobile_number":mobile_number,"email_address":email_address,"date_of_birth":date_of_birth}])

        except Exception as e:
            print(f"{e} exception occurs")


# create_new_record()
# update_info("cba","hello@gmail.com","9897979798","2000-04-01")
# print(models.execute_kw(db, uid, password, 'patients.description', 'name_search', []))
# fetch_patients_name()
# fetch_full_data()