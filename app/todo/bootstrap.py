from todo import unit_of_work



class MessageBus:
    def __init__(
        self,
        uow: unit_of_work.AbstractUnitOfWork,
    ):
       self.uow = uow


def bootstrap(
    uow: unit_of_work.AbstractUnitOfWork = unit_of_work.SqlAlchemyUnitOfWork(),
) -> MessageBus:

    return MessageBus(
        uow=uow,
    )
