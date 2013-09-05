#!env/bin/python
import bottle
import argparse
import routes
import config

def migrate(args):
    import model
    from model.base import Base
    Base.metadata.create_all(config.engine)

def seed(args):
    import seed
    seed.seed()

def serve(args):
    bottle.run(port=config.port, reloader=config.use_reloader)

parser = argparse.ArgumentParser()
subs = parser.add_subparsers()

subs.add_parser('migrate').set_defaults(func=migrate)
subs.add_parser('seed').set_defaults(func=seed)
subs.add_parser('serve').set_defaults(func=serve)

args = parser.parse_args()
args.func(args)