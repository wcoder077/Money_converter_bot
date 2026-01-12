from aiogram.fsm.state import State, StatesGroup


class ConvertState(StatesGroup):
    from_cur = State()
    to_cur = State()
    how_much = State()
    result = State()


class OfferState(StatesGroup):
    offer = State()
