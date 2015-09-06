#!/usr/bin/env python

__author__ = 'Tran Huu Cuong'

import click


@click.command()
@click.argument('query', required=True)
@click.option('--raw-result/--no-raw-result', default=False)
def search(query, raw_result):
    print('query: {}'.format(query))
    print('raw-result: {}'.format(raw_result))


if __name__ == '__main__':
    search()



