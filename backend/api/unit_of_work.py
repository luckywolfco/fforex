from __future__ import annotations
import abc
from django.db import transaction


class UnitOfWork(abc.ABC):
    def __enter__(self):
        transaction.set_autocommit(False)
        return

    def __exit__(self, *args):
        transaction.set_autocommit(True)

    def commit(self):
        transaction.commit()

    def rollback(self):
        transaction.rollback()
