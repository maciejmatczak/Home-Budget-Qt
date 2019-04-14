from sqlalchemy import (Boolean, Column, Date, Float, ForeignKey, Integer,
                        String, create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///:memory:')
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    estimate = Column(Float, nullable=False)


class BudgetRule(Base):
    __tablename__ = 'budget_rules'

    id = Column(Integer, primary_key=True)
    sentence = Column(String, nullable=False)
    estimate = Column(Float, nullable=False)
    category_id = Column(
        Integer,
        ForeignKey('categories.id', onupdate='CASCADE', ondelete='SET NULL')
    )
    category = relationship('Category')


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    new = Column(Boolean)
    account_date = Column(Date, nullable=False)
    operation_date = Column(Date)
    details = Column(String)
    account_no = Column(String)
    title = Column(String)
    amount = Column(Float, nullable=False)
    currency = Column(String)
    ref_number = Column(String)
    operation_type = Column(String)
    note = Column(String)
    category_id = Column(
        Integer,
        ForeignKey('categories.id', onupdate='CASCADE', ondelete='SET NULL')
    )
    category = relationship('Category')


def mockup():
    global session

    from datetime import date, timedelta
    import random

    for name in ['?', 'Car', 'Grocery']:
        category = Category(
            name=name,
            date=date(2019, 4, 1),
            estimate=-12.34
        )

        session.add(category)

    session.commit()

    categories = Category.query.all()

    for i in range(30):
        transaction = Transaction(
            account_date=date(2018, 5, 1) + timedelta(days=i),
            category=random.choice(categories),
            amount=-12.34
        )

        session.add(transaction)

    session.commit()


if __name__ == "__main__":
    mockup()
