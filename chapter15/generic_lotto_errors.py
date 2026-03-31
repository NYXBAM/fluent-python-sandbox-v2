from generic_lotto import LottoBlower

machine = LottoBlower[int]([1, .2]) # mypy generic_lotto_errors.py
# generic_lotto_errors.py:3: error: Argument 1 to "LottoBlower" has incompatible type "List[object]"; expected "Iterable[int]"  [arg-type]


machine = LottoBlower[int](range(1, 11))

machine.load('ABC') # mypy generic_lotto_errors.py
# generic_lotto_errors.py:7: error: Argument 1 to "load" of "LottoBlower" has incompatible type "str"; expected "Iterable[int]"  [arg-type]
