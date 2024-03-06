from typing import Any, Callable, ParamSpec, TypeVar, Union, overload

_InputParams = ParamSpec("_InputParams")


_Out0 = TypeVar("_Out0")
_Out1 = TypeVar("_Out1")
_Out2 = TypeVar("_Out2")
_Out3 = TypeVar("_Out3")
_Out4 = TypeVar("_Out4")
_Out5 = TypeVar("_Out5")
_Out6 = TypeVar("_Out6")
_Out7 = TypeVar("_Out7")
_Out8 = TypeVar("_Out8")
_Out9 = TypeVar("_Out9")
_Out10 = TypeVar("_Out10")
_Out11 = TypeVar("_Out11")
_Out12 = TypeVar("_Out12")
_Out13 = TypeVar("_Out13")
_Out14 = TypeVar("_Out14")
_Out15 = TypeVar("_Out15")
_Out16 = TypeVar("_Out16")
_Out17 = TypeVar("_Out17")
_Out18 = TypeVar("_Out18")
_Out19 = TypeVar("_Out19")


@overload
def compose(op0: Callable[_InputParams, _Out0], /) -> Callable[_InputParams, _Out0]: ...


@overload
def compose(
    op0: Callable[_InputParams, _Out0], op1: Callable[[_Out0], _Out1], /
) -> Callable[_InputParams, _Out1]: ...


@overload
def compose(
    op0: Callable[_InputParams, _Out0],
    op1: Callable[[_Out0], _Out1],
    op2: Callable[[_Out1], _Out2],
    /,
) -> Callable[_InputParams, _Out2]: ...


@overload
def compose(
    op0: Callable[_InputParams, _Out0],
    op1: Callable[[_Out0], _Out1],
    op2: Callable[[_Out1], _Out2],
    op3: Callable[[_Out2], _Out3],
    /,
) -> Callable[_InputParams, _Out3]: ...


@overload
def compose(
    op0: Callable[_InputParams, _Out0],
    op1: Callable[[_Out0], _Out1],
    op2: Callable[[_Out1], _Out2],
    op3: Callable[[_Out2], _Out3],
    op4: Callable[[_Out3], _Out4],
    /,
) -> Callable[_InputParams, _Out4]: ...


@overload
def compose(
    op0: Callable[_InputParams, _Out0],
    op1: Callable[[_Out0], _Out1],
    op2: Callable[[_Out1], _Out2],
    op3: Callable[[_Out2], _Out3],
    op4: Callable[[_Out3], _Out4],
    op5: Callable[[_Out4], _Out5],
    /,
) -> Callable[_InputParams, _Out5]: ...


@overload
def compose(
    op0: Callable[_InputParams, _Out0],
    op1: Callable[[_Out0], _Out1],
    op2: Callable[[_Out1], _Out2],
    op3: Callable[[_Out2], _Out3],
    op4: Callable[[_Out3], _Out4],
    op5: Callable[[_Out4], _Out5],
    op6: Callable[[_Out5], _Out6],
    /,
) -> Callable[_InputParams, _Out6]: ...


@overload
def compose(
    op0: Callable[_InputParams, _Out0],
    op1: Callable[[_Out0], _Out1],
    op2: Callable[[_Out1], _Out2],
    op3: Callable[[_Out2], _Out3],
    op4: Callable[[_Out3], _Out4],
    op5: Callable[[_Out4], _Out5],
    op6: Callable[[_Out5], _Out6],
    op7: Callable[[_Out6], _Out7],
    /,
) -> Callable[_InputParams, _Out7]: ...


@overload
def compose(
    op0: Callable[_InputParams, _Out0],
    op1: Callable[[_Out0], _Out1],
    op2: Callable[[_Out1], _Out2],
    op3: Callable[[_Out2], _Out3],
    op4: Callable[[_Out3], _Out4],
    op5: Callable[[_Out4], _Out5],
    op6: Callable[[_Out5], _Out6],
    op7: Callable[[_Out6], _Out7],
    op8: Callable[[_Out7], _Out8],
    /,
) -> Callable[_InputParams, _Out8]: ...


@overload
def compose(
    op0: Callable[_InputParams, _Out0],
    op1: Callable[[_Out0], _Out1],
    op2: Callable[[_Out1], _Out2],
    op3: Callable[[_Out2], _Out3],
    op4: Callable[[_Out3], _Out4],
    op5: Callable[[_Out4], _Out5],
    op6: Callable[[_Out5], _Out6],
    op7: Callable[[_Out6], _Out7],
    op8: Callable[[_Out7], _Out8],
    op9: Callable[[_Out8], _Out9],
    /,
) -> Callable[_InputParams, _Out9]: ...


@overload
def compose(
    op0: Callable[_InputParams, _Out0],
    op1: Callable[[_Out0], _Out1],
    op2: Callable[[_Out1], _Out2],
    op3: Callable[[_Out2], _Out3],
    op4: Callable[[_Out3], _Out4],
    op5: Callable[[_Out4], _Out5],
    op6: Callable[[_Out5], _Out6],
    op7: Callable[[_Out6], _Out7],
    op8: Callable[[_Out7], _Out8],
    op9: Callable[[_Out8], _Out9],
    op10: Callable[[_Out9], _Out10],
    /,
) -> Callable[_InputParams, _Out10]: ...


@overload
def compose(
    op0: Callable[_InputParams, _Out0],
    op1: Callable[[_Out0], _Out1],
    op2: Callable[[_Out1], _Out2],
    op3: Callable[[_Out2], _Out3],
    op4: Callable[[_Out3], _Out4],
    op5: Callable[[_Out4], _Out5],
    op6: Callable[[_Out5], _Out6],
    op7: Callable[[_Out6], _Out7],
    op8: Callable[[_Out7], _Out8],
    op9: Callable[[_Out8], _Out9],
    op10: Callable[[_Out9], _Out10],
    op11: Callable[[_Out10], _Out11],
    /,
) -> Callable[_InputParams, _Out11]: ...


@overload
def compose(
    op0: Callable[_InputParams, _Out0],
    op1: Callable[[_Out0], _Out1],
    op2: Callable[[_Out1], _Out2],
    op3: Callable[[_Out2], _Out3],
    op4: Callable[[_Out3], _Out4],
    op5: Callable[[_Out4], _Out5],
    op6: Callable[[_Out5], _Out6],
    op7: Callable[[_Out6], _Out7],
    op8: Callable[[_Out7], _Out8],
    op9: Callable[[_Out8], _Out9],
    op10: Callable[[_Out9], _Out10],
    op11: Callable[[_Out10], _Out11],
    op12: Callable[[_Out11], _Out12],
    /,
) -> Callable[_InputParams, _Out12]: ...


@overload
def compose(
    op0: Callable[_InputParams, _Out0],
    op1: Callable[[_Out0], _Out1],
    op2: Callable[[_Out1], _Out2],
    op3: Callable[[_Out2], _Out3],
    op4: Callable[[_Out3], _Out4],
    op5: Callable[[_Out4], _Out5],
    op6: Callable[[_Out5], _Out6],
    op7: Callable[[_Out6], _Out7],
    op8: Callable[[_Out7], _Out8],
    op9: Callable[[_Out8], _Out9],
    op10: Callable[[_Out9], _Out10],
    op11: Callable[[_Out10], _Out11],
    op12: Callable[[_Out11], _Out12],
    op13: Callable[[_Out12], _Out13],
    /,
) -> Callable[_InputParams, _Out13]: ...


@overload
def compose(
    op0: Callable[_InputParams, _Out0],
    op1: Callable[[_Out0], _Out1],
    op2: Callable[[_Out1], _Out2],
    op3: Callable[[_Out2], _Out3],
    op4: Callable[[_Out3], _Out4],
    op5: Callable[[_Out4], _Out5],
    op6: Callable[[_Out5], _Out6],
    op7: Callable[[_Out6], _Out7],
    op8: Callable[[_Out7], _Out8],
    op9: Callable[[_Out8], _Out9],
    op10: Callable[[_Out9], _Out10],
    op11: Callable[[_Out10], _Out11],
    op12: Callable[[_Out11], _Out12],
    op13: Callable[[_Out12], _Out13],
    op14: Callable[[_Out13], _Out14],
    /,
) -> Callable[_InputParams, _Out14]: ...


@overload
def compose(
    op0: Callable[_InputParams, _Out0],
    op1: Callable[[_Out0], _Out1],
    op2: Callable[[_Out1], _Out2],
    op3: Callable[[_Out2], _Out3],
    op4: Callable[[_Out3], _Out4],
    op5: Callable[[_Out4], _Out5],
    op6: Callable[[_Out5], _Out6],
    op7: Callable[[_Out6], _Out7],
    op8: Callable[[_Out7], _Out8],
    op9: Callable[[_Out8], _Out9],
    op10: Callable[[_Out9], _Out10],
    op11: Callable[[_Out10], _Out11],
    op12: Callable[[_Out11], _Out12],
    op13: Callable[[_Out12], _Out13],
    op14: Callable[[_Out13], _Out14],
    op15: Callable[[_Out14], _Out15],
    /,
) -> Callable[_InputParams, _Out15]: ...


@overload
def compose(
    op0: Callable[_InputParams, _Out0],
    op1: Callable[[_Out0], _Out1],
    op2: Callable[[_Out1], _Out2],
    op3: Callable[[_Out2], _Out3],
    op4: Callable[[_Out3], _Out4],
    op5: Callable[[_Out4], _Out5],
    op6: Callable[[_Out5], _Out6],
    op7: Callable[[_Out6], _Out7],
    op8: Callable[[_Out7], _Out8],
    op9: Callable[[_Out8], _Out9],
    op10: Callable[[_Out9], _Out10],
    op11: Callable[[_Out10], _Out11],
    op12: Callable[[_Out11], _Out12],
    op13: Callable[[_Out12], _Out13],
    op14: Callable[[_Out13], _Out14],
    op15: Callable[[_Out14], _Out15],
    op16: Callable[[_Out15], _Out16],
    /,
) -> Callable[_InputParams, _Out16]: ...


@overload
def compose(
    op0: Callable[_InputParams, _Out0],
    op1: Callable[[_Out0], _Out1],
    op2: Callable[[_Out1], _Out2],
    op3: Callable[[_Out2], _Out3],
    op4: Callable[[_Out3], _Out4],
    op5: Callable[[_Out4], _Out5],
    op6: Callable[[_Out5], _Out6],
    op7: Callable[[_Out6], _Out7],
    op8: Callable[[_Out7], _Out8],
    op9: Callable[[_Out8], _Out9],
    op10: Callable[[_Out9], _Out10],
    op11: Callable[[_Out10], _Out11],
    op12: Callable[[_Out11], _Out12],
    op13: Callable[[_Out12], _Out13],
    op14: Callable[[_Out13], _Out14],
    op15: Callable[[_Out14], _Out15],
    op16: Callable[[_Out15], _Out16],
    op17: Callable[[_Out16], _Out17],
    /,
) -> Callable[_InputParams, _Out17]: ...


@overload
def compose(
    op0: Callable[_InputParams, _Out0],
    op1: Callable[[_Out0], _Out1],
    op2: Callable[[_Out1], _Out2],
    op3: Callable[[_Out2], _Out3],
    op4: Callable[[_Out3], _Out4],
    op5: Callable[[_Out4], _Out5],
    op6: Callable[[_Out5], _Out6],
    op7: Callable[[_Out6], _Out7],
    op8: Callable[[_Out7], _Out8],
    op9: Callable[[_Out8], _Out9],
    op10: Callable[[_Out9], _Out10],
    op11: Callable[[_Out10], _Out11],
    op12: Callable[[_Out11], _Out12],
    op13: Callable[[_Out12], _Out13],
    op14: Callable[[_Out13], _Out14],
    op15: Callable[[_Out14], _Out15],
    op16: Callable[[_Out15], _Out16],
    op17: Callable[[_Out16], _Out17],
    op18: Callable[[_Out17], _Out18],
    /,
) -> Callable[_InputParams, _Out18]: ...


def compose(op0: Callable[_InputParams, _Out0], op1: Union[Callable[[_Out0], _Out1], None] = None, op2: Union[Callable[[_Out1], _Out2], None] = None, op3: Union[Callable[[_Out2], _Out3], None] = None, op4: Union[Callable[[_Out3], _Out4], None] = None, op5: Union[Callable[[_Out4], _Out5], None] = None, op6: Union[Callable[[_Out5], _Out6], None] = None, op7: Union[Callable[[_Out6], _Out7], None] = None, op8: Union[Callable[[_Out7], _Out8], None] = None, op9: Union[Callable[[_Out8], _Out9], None] = None, op10: Union[Callable[[_Out9], _Out10], None] = None, op11: Union[Callable[[_Out10], _Out11], None] = None, op12: Union[Callable[[_Out11], _Out12], None] = None, op13: Union[Callable[[_Out12], _Out13], None] = None, op14: Union[Callable[[_Out13], _Out14], None] = None, op15: Union[Callable[[_Out14], _Out15], None] = None, op16: Union[Callable[[_Out15], _Out16], None] = None, op17: Union[Callable[[_Out16], _Out17], None] = None, op18: Union[Callable[[_Out17], _Out18], None] = None, op19: Union[Callable[[_Out18], _Out19], None] = None, /) -> Callable[_InputParams, Any]:  # type: ignore
    """
    Pipeline takes up to 20 functions and composites them into a single function.
    """

    if not op1:

        def _inner0(*args: _InputParams.args, **kwargs: _InputParams.kwargs) -> _Out0:
            return op0(*args, **kwargs)  # fmt: skip

        return _inner0

    elif not op2:

        def _inner1(*args: _InputParams.args, **kwargs: _InputParams.kwargs) -> _Out1:
            return op1(op0(*args, **kwargs))  # fmt: skip

        return _inner1

    elif not op3:

        def _inner2(*args: _InputParams.args, **kwargs: _InputParams.kwargs) -> _Out2:
            return op2(op1(op0(*args, **kwargs)))  # fmt: skip

        return _inner2

    elif not op4:

        def _inner3(*args: _InputParams.args, **kwargs: _InputParams.kwargs) -> _Out3:
            return op3(op2(op1(op0(*args, **kwargs))))  # fmt: skip

        return _inner3

    elif not op5:

        def _inner4(*args: _InputParams.args, **kwargs: _InputParams.kwargs) -> _Out4:
            return op4(op3(op2(op1(op0(*args, **kwargs)))))  # fmt: skip

        return _inner4

    elif not op6:

        def _inner5(*args: _InputParams.args, **kwargs: _InputParams.kwargs) -> _Out5:
            return op5(op4(op3(op2(op1(op0(*args, **kwargs))))))  # fmt: skip

        return _inner5

    elif not op7:

        def _inner6(*args: _InputParams.args, **kwargs: _InputParams.kwargs) -> _Out6:
            return op6(op5(op4(op3(op2(op1(op0(*args, **kwargs)))))))  # fmt: skip

        return _inner6

    elif not op8:

        def _inner7(*args: _InputParams.args, **kwargs: _InputParams.kwargs) -> _Out7:
            return op7(op6(op5(op4(op3(op2(op1(op0(*args, **kwargs))))))))  # fmt: skip

        return _inner7

    elif not op9:

        def _inner8(*args: _InputParams.args, **kwargs: _InputParams.kwargs) -> _Out8:
            return op8(op7(op6(op5(op4(op3(op2(op1(op0(*args, **kwargs)))))))))  # fmt: skip

        return _inner8

    elif not op10:

        def _inner9(*args: _InputParams.args, **kwargs: _InputParams.kwargs) -> _Out9:
            return op9(op8(op7(op6(op5(op4(op3(op2(op1(op0(*args, **kwargs))))))))))  # fmt: skip

        return _inner9

    elif not op11:

        def _inner10(*args: _InputParams.args, **kwargs: _InputParams.kwargs) -> _Out10:
            return op10(op9(op8(op7(op6(op5(op4(op3(op2(op1(op0(*args, **kwargs)))))))))))  # fmt: skip

        return _inner10

    elif not op12:

        def _inner11(*args: _InputParams.args, **kwargs: _InputParams.kwargs) -> _Out11:
            return op11(op10(op9(op8(op7(op6(op5(op4(op3(op2(op1(op0(*args, **kwargs))))))))))))  # fmt: skip

        return _inner11

    elif not op13:

        def _inner12(*args: _InputParams.args, **kwargs: _InputParams.kwargs) -> _Out12:
            return op12(op11(op10(op9(op8(op7(op6(op5(op4(op3(op2(op1(op0(*args, **kwargs)))))))))))))  # fmt: skip

        return _inner12

    elif not op14:

        def _inner13(*args: _InputParams.args, **kwargs: _InputParams.kwargs) -> _Out13:
            return op13(op12(op11(op10(op9(op8(op7(op6(op5(op4(op3(op2(op1(op0(*args, **kwargs))))))))))))))  # fmt: skip

        return _inner13

    elif not op15:

        def _inner14(*args: _InputParams.args, **kwargs: _InputParams.kwargs) -> _Out14:
            return op14(op13(op12(op11(op10(op9(op8(op7(op6(op5(op4(op3(op2(op1(op0(*args, **kwargs)))))))))))))))  # fmt: skip

        return _inner14

    elif not op16:

        def _inner15(*args: _InputParams.args, **kwargs: _InputParams.kwargs) -> _Out15:
            return op15(op14(op13(op12(op11(op10(op9(op8(op7(op6(op5(op4(op3(op2(op1(op0(*args, **kwargs))))))))))))))))  # fmt: skip

        return _inner15

    elif not op17:

        def _inner16(*args: _InputParams.args, **kwargs: _InputParams.kwargs) -> _Out16:
            return op16(op15(op14(op13(op12(op11(op10(op9(op8(op7(op6(op5(op4(op3(op2(op1(op0(*args, **kwargs)))))))))))))))))  # fmt: skip

        return _inner16

    elif not op18:

        def _inner17(*args: _InputParams.args, **kwargs: _InputParams.kwargs) -> _Out17:
            return op17(op16(op15(op14(op13(op12(op11(op10(op9(op8(op7(op6(op5(op4(op3(op2(op1(op0(*args, **kwargs))))))))))))))))))  # fmt: skip

        return _inner17

    elif not op19:

        def _inner18(*args: _InputParams.args, **kwargs: _InputParams.kwargs) -> _Out18:
            return op18(op17(op16(op15(op14(op13(op12(op11(op10(op9(op8(op7(op6(op5(op4(op3(op2(op1(op0(*args, **kwargs)))))))))))))))))))  # fmt: skip

        return _inner18

    else:

        def _inner19(*args: _InputParams.args, **kwargs: _InputParams.kwargs) -> _Out19:
            return op19(op18(op17(op16(op15(op14(op13(op12(op11(op10(op9(op8(op7(op6(op5(op4(op3(op2(op1(op0(*args, **kwargs))))))))))))))))))))  # fmt: skip

        return _inner19
