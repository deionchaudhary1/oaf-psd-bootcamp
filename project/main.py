import argparse
from security import SecurityHandler
from project import ServiceFactory, Environment

class Handler:
    def __init__(self, service): #the service will be injected
        self.sv = service

    def display(self):
        '''
        This method takes the data of the given job link and prints it out
        '''
        values = self.sv.get_job_data()
            #returns the 2d array
        print(values)

def data_call():
    #... creating factories
     #API
    api_factory = ServiceFactory()
    api = api_factory.create_service(Environment.PROD) #api is the instance of the API Service
    ans = Handler(api)
    ans.display() #returns the data
    

    #MOCK
    mock_factory = ServiceFactory()
    mock = mock_factory.create_service(Environment.TEST)
    mo = Handler(mock)
    mo.display() #returns the data

#def endpoints():



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Job Parser')
    parser.add_argument("--username", "-u", help="Username for login", required=True)
    parser.add_argument("--password", "-p", help="Password for login", required=True)
    parser.add_argument("--setup", help="Mode to run the program in ('run' or 'setup')", action='store_true')
    parser.add_argument("--reset", help="Reset the database", action='store_true')
    args = parser.parse_args()

    login = SecurityHandler()
    if not args.setup:
        if login.login_user(args.username, args.password):
            data_call()
        else:
            print("Invalid credentials")
    elif args.reset:
        login.reset_database()
    else:
        login.create_user(args.username, args.password)
    
    login.close_connection()