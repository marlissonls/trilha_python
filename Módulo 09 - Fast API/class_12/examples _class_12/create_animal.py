from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


# https://docs.sqlalchemy.org/en/20/orm/quickstart.html#create-an-engine
engine = create_engine('sqlite:///:memory:', echo=True) # echo=True repete no console o comando em Python e depois equivalente em SQL
# engine = create_engine('sqlite:///pets.db', echo=True)
# engine = create_engine('postgresql://user:password@host:port/database', echo=True)

Base = declarative_base()

class Pet(Base):

    __tablename__ = 'pets'
    id = Column(Integer, primary_key=True)
    petNome = Column(String)
    petIdade = Column(Integer)
    petTipo = Column(String)

    def __repr__(self):
        return f'{self.id} | {self.petNome} {self.petIdade} {self.petTipo}'
    
# Criação da tabela no banco de dados em memória
Base.metadata.create_all(engine)

# Criação de uma sessão para interagir com o banco de dados
Session = sessionmaker(bind=engine)
session = Session()

# Inserção de um novo Pet na tabela em memória
new_pet = Pet(petNome='Whiskers', petIdade=2, petTipo='Gato')
session.add(new_pet)
session.commit()

# Consulta e impressão de todos os Pets na tabela em memória
pets = session.query(Pet).all()
for pet in pets:
    print(pet)

# Fechamento da sessão
session.close()