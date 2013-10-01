import common
import buckit.model as m
from buckit.utils import with_session
from sqlalchemy.orm import joinedload
import table_print

def setup_parser(parent_parser):
    p = parent_parser.add_parser('accounts')
    p.set_defaults(func=show_accounts)

    p = parent_parser.add_parser('payees')
    p.set_defaults(func=show_payees)

    p = parent_parser.add_parser('ledger')
    p.add_argument('--account', '-a', required=True)
    p.set_defaults(func=show_ledger)

@with_session
def show_accounts(session, args):
    accounts = session.query(m.Account).all()
    table = [(a.id, a.name, a.type,) for a in accounts]
    table_print.p(table, header=('id', 'name', 'type',))

@with_session
def show_payees(session, args):
    payees = session.query(m.Payee).all()
    table = [(p.id, p.name,) for p in payees]
    table_print.p(table, header=('id', 'name',))

@with_session
def show_ledger(session, args):
    account = common.search_by_name(session, m.Account, args.account)
    splits = session.query(m.Split)\
        .join(m.Account)\
        .join(m.Transaction)\
        .filter(m.Account.name == args.account)\
        .order_by(m.Transaction.date.desc())\
        .all()

    table = []
    for split in splits:
        transaction = split.transaction
        table.append((
            transaction.id,
            transaction.date,
            transaction.payee.name if transaction.payee else '',
            split.amount,
        ))

    table_print.p(table, header=('id', 'date', 'payee', 'amount',))
