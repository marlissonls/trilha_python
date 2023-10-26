from sqlalchemy import create_engine, Column, String, Integer, Float, Date
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import date

engine = create_engine('sqlite:///:memory:', echo=True)

Base = declarative_base()

class Book(Base):

    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column('Title', String)
    author = Column('Author', String)
    published_date = Column('Published', Date)
    price = Column('Price', Float)

    def __repr__(self):
        return f'<Title: {self.title} | Author: {self.author} | Published: {self.published_date} | Price: {self.price}>'
    

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

if __name__ == '__main__':

    new_book = Book(title='John Doe', author='John A. Doe', published_date=date(2023, 8, 1), price='7.99')
    new_book2 = Book(title='Some Book', author='Doe', published_date=date(2023, 2, 22), price='10.99')
    session.add(new_book)
    session.add(new_book2)
    session.commit()


    books = session.query(Book).all()
    for book in books:
        print(book)
