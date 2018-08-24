from sqlalchemy import Column, Integer, String, DateTime, Float
from database import Base

class test_metadata(Base):
    
    __tablename__ = 'test_metadata'
    date = Column('date', DateTime, primary_key = True)
    time_stamp = Column('time_stamp', DateTime)
    size = Column('size', Float)
    n_att = Column('n_att', Float)
    n_row = Column('n_row', Float)
    flag = Column('flag', String(10))
    header = Column('header', String(100))

    def __init__(self, name=None, email=None):
        self.date = date
        self.time_stamp = time_stamp
        self.size = size
        self.n_att = n_att
        self.n_row = n_row
        self.flag = flag
        self.header = header

    def __repr__(self):
        return '<test_metadata %r>' % (self.date)

    #https://docs.sqlalchemy.org/en/latest/orm/mapped_sql_expr.html#mapper-sql-expressions

    
