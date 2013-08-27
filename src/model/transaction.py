import base
from sqlalchemy import Column, ForeignKey, Integer, Date, Enum
from sqlalchemy.orm import relationship

TransactionStatus = Enum(
    'not_reconciled',
    'cleared',
    'reconciled',
    name='transaction_status',
)

class Transaction(base.Base):

    __tablename__ = 'transactions'

    id         = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('accounts.id'))
    date       = Column(Date, nullable=False)
    status     = Column(TransactionStatus)

    account = relationship('Account')
    splits = relationship('Split')

    def __json__(self):
        return {
            'id':      self.id,
            'account': self.account,
            'date':    self.date,
            'status':  self.status,
            'splits':  self.splits,
        }

    def __repr__(self):
        return "<Transaction ('{0}')".format(self.id)
