from typing import List, Optional
from sqlalchemy import ForeignKey, String, create_engine
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker
from sqlalchemy.orm.decl_api import mapped_column

class Base(DeclarativeBase):
    pass

class User(Base):

    __tablename__ = "user_account"
    id = mapped_column(int, primary_key=True)
    name = mapped_column(String(30))
    fullname = mapped_column(String)
    addresses = relationship("Address", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"
    
class Address(Base):

    __tablename__ = "address"
    id = mapped_column(int, primary_key=True)
    email_address = mapped_column(String)
    user_id = mapped_column(int, ForeignKey("user_account.id"))
    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"
    

engine = create_engine('sqlite:///:memory:', echo=True)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

if __name__ == '__main__':
    # Inserção de um novo usuário e seu endereço associado
    new_user = User(name='John Doe', fullname='John A. Doe')
    new_address = Address(email_address='john.doe@example.com', user=new_user)
    session.add(new_user)
    session.commit()

    # Consulta de todos os usuários e seus endereços associados
    users = session.query(User).all()
    for user in users:
        print(user)
        for address in user.addresses:
            print(address)

    session.close()
