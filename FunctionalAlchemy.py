
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker


#Creating DB with engine
engine=create_engine("sqlite:///usersf.db", echo=True)
Base=declarative_base()

class User(Base):
    __tablename__="users"
    id=Column(Integer, primary_key=True, autoincrement=True)
    name=Column(String, nullable=False)
    age = Column(Integer, nullable=False)

Base.metadata.create_all(engine)

Session=sessionmaker(bind=engine)
session=Session()

#Functions
def getAllUsers():
    users=session.query(User).all()
    return users

def displayAllUsers(users):
    users=getAllUsers()
    if users:
        for user in users:
            print(user.id, user.name, user.age)
    else:
        print("No Users Found!")

def addNewUser(name,age):
    user=User(name=name, age=age)
    newUser=session.add(user)
    session.commit()
    if user.id:
        return f'User added Successfully with id {user.id}'
    else:
        return "Failed to added User"

def findById(id):
    return session.query(User).filter_by(id=id).first()

def findAllByName(name):
    return session.query(User).filter_by(name=name).all()


def findFirstByName(name):
    return session.query(User).filter_by(name=name).first()

def findAllByAge(age):
    return session.query(User).filter_by(age=age).all()

def updateNameById(id, name):
    user = findById(id)
    if user:
        user.name=name
        session.commit()
        return user
    else: 
        return 'User is not found'

def UpdateAllNameByName(name, newName):
    users = findAllByName(name)
    if users:
        for user in users:
            user.name=newName
        session.commit()
        return users
    else:
        return "Users are not found!"

def updateNameById(id, name):
    user = findById(id)
    if user:
        user.name=name
        session.commit()
        return user
    else:
        return "User is not found!"

def updateAgeById(id,newAge):
    user = findById(id)
    if user: 
        user.age=newAge
        session.commit()
        return user
    else:
        return "User not found!"


def delById(id):
    user = findById(id)
    if user: 
        session.delete(user)
        session.commit()
        return "User deleted Successfully. "
    else:
        return "User not found!"

def delFirstByName(name):
    user = findFirstByName(name)
    if user: 
        session.delete(user)
        session.commit()
        return "User deleted Successfully. "
    else:
        return "User not found!"


def delAllByName(name):
    users=findAllByName(name)
    if users:
        for user in users:
            session.delete(user)
        session.commit()
        return f"Deleted Users with Name: {name}"
    else:
        return "User not found!"

    
def delAll():
    users=getAllUsers()
    if users:
        for user in users:
            session.delete(user)
        session.commit()
        return f"Deleted All Users"
    else:
        return "Database is empty!"


    
if __name__=="__main__":
    # Example usage
    print("+==>",getAllUsers())
    print("+==>",addNewUser("John", 30))
    print("+==>",addNewUser("Jane", 25))
    print("+==>",displayAllUsers())
    print("+==>",findById(1))
    print("+==>",findAllByName("John"))
    print("+==>",findFirstByName("Jane"))
    print("+==>",findAllByAge(30))
    print("+==>",updateNameById(1, "Johnny"))
    print("+==>",UpdateAllNameByName("Jane", "Janet"))
    print("+==>",updateAgeById(2, 26))
    print("+==>",delById(1))
    print("+==>",delFirstByName("Janet"))
    print("+==>",delAllByName("Jane"))
    print("+==>",delAll())


