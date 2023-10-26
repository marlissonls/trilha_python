from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user_account"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String)
    addresses = relationship("Address", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"
    
class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    email_address = Column(String)
    user_id = Column(Integer, ForeignKey("user_account.id"))
    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return f"Address(id={self.id!r}, user_id={self.user_id!r}, email_address={self.email_address!r})"
    

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
