from typing import Any, Callable, TypeVar, Union, overload

_InputVal = TypeVar("_InputVal")
_DefaultCallable = Union[Callable[..., Any], None]


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
def pipe(value: _InputVal, op0: Callable[[_InputVal], _Out0], /) -> _Out0: ...


@overload
def pipe(
    value: _InputVal,
    op0: Callable[[_InputVal], _Out0],
    op1: Callable[[_Out0], _Out1],
    /,
) -> _Out1: ...


@overload
def pipe(
    value: _InputVal,
    op0: Callable[[_InputVal], _Out0],
    op1: Callable[[_Out0], _Out1],
    op2: Callable[[_Out1], _Out2],
    /,
) -> _Out2: ...


@overload
def pipe(
    value: _InputVal,
    op0: Callable[[_InputVal], _Out0],
    op1: Callable[[_Out0], _Out1],
    op2: Callable[[_Out1], _Out2],
    op3: Callable[[_Out2], _Out3],
    /,
) -> _Out3: ...


@overload
def pipe(
    value: _InputVal,
    op0: Callable[[_InputVal], _Out0],
    op1: Callable[[_Out0], _Out1],
    op2: Callable[[_Out1], _Out2],
    op3: Callable[[_Out2], _Out3],
    op4: Callable[[_Out3], _Out4],
    /,
) -> _Out4: ...


@overload
def pipe(
    value: _InputVal,
    op0: Callable[[_InputVal], _Out0],
    op1: Callable[[_Out0], _Out1],
    op2: Callable[[_Out1], _Out2],
    op3: Callable[[_Out2], _Out3],
    op4: Callable[[_Out3], _Out4],
    op5: Callable[[_Out4], _Out5],
    /,
) -> _Out5: ...


@overload
def pipe(
    value: _InputVal,
    op0: Callable[[_InputVal], _Out0],
    op1: Callable[[_Out0], _Out1],
    op2: Callable[[_Out1], _Out2],
    op3: Callable[[_Out2], _Out3],
    op4: Callable[[_Out3], _Out4],
    op5: Callable[[_Out4], _Out5],
    op6: Callable[[_Out5], _Out6],
    /,
) -> _Out6: ...


@overload
def pipe(
    value: _InputVal,
    op0: Callable[[_InputVal], _Out0],
    op1: Callable[[_Out0], _Out1],
    op2: Callable[[_Out1], _Out2],
    op3: Callable[[_Out2], _Out3],
    op4: Callable[[_Out3], _Out4],
    op5: Callable[[_Out4], _Out5],
    op6: Callable[[_Out5], _Out6],
    op7: Callable[[_Out6], _Out7],
    /,
) -> _Out7: ...


@overload
def pipe(
    value: _InputVal,
    op0: Callable[[_InputVal], _Out0],
    op1: Callable[[_Out0], _Out1],
    op2: Callable[[_Out1], _Out2],
    op3: Callable[[_Out2], _Out3],
    op4: Callable[[_Out3], _Out4],
    op5: Callable[[_Out4], _Out5],
    op6: Callable[[_Out5], _Out6],
    op7: Callable[[_Out6], _Out7],
    op8: Callable[[_Out7], _Out8],
    /,
) -> _Out8: ...


@overload
def pipe(
    value: _InputVal,
    op0: Callable[[_InputVal], _Out0],
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
) -> _Out9: ...


@overload
def pipe(
    value: _InputVal,
    op0: Callable[[_InputVal], _Out0],
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
) -> _Out10: ...


@overload
def pipe(
    value: _InputVal,
    op0: Callable[[_InputVal], _Out0],
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
) -> _Out11: ...


@overload
def pipe(
    value: _InputVal,
    op0: Callable[[_InputVal], _Out0],
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
) -> _Out12: ...


@overload
def pipe(
    value: _InputVal,
    op0: Callable[[_InputVal], _Out0],
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
) -> _Out13: ...


@overload
def pipe(
    value: _InputVal,
    op0: Callable[[_InputVal], _Out0],
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
) -> _Out14: ...


@overload
def pipe(
    value: _InputVal,
    op0: Callable[[_InputVal], _Out0],
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
) -> _Out15: ...


@overload
def pipe(
    value: _InputVal,
    op0: Callable[[_InputVal], _Out0],
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
) -> _Out16: ...


@overload
def pipe(
    value: _InputVal,
    op0: Callable[[_InputVal], _Out0],
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
) -> _Out17: ...


@overload
def pipe(
    value: _InputVal,
    op0: Callable[[_InputVal], _Out0],
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
) -> _Out18: ...


def pipe(value: Any, op0: _DefaultCallable = None, op1: _DefaultCallable = None, op2: _DefaultCallable = None, op3: _DefaultCallable = None, op4: _DefaultCallable = None, op5: _DefaultCallable = None, op6: _DefaultCallable = None, op7: _DefaultCallable = None, op8: _DefaultCallable = None, op9: _DefaultCallable = None, op10: _DefaultCallable = None, op11: _DefaultCallable = None, op12: _DefaultCallable = None, op13: _DefaultCallable = None, op14: _DefaultCallable = None, op15: _DefaultCallable = None, op16: _DefaultCallable = None, op17: _DefaultCallable = None, op18: _DefaultCallable = None, op19: _DefaultCallable = None, /) -> Any:  # type: ignore
    """
    Pipe takes up to 20 functions and applies them to a value.
    """

    if not op0:
        return value  # fmt: skip

    elif not op1:
        return op0(value)  # fmt: skip

    elif not op2:
        return op1(op0(value))  # fmt: skip

    elif not op3:
        return op2(op1(op0(value)))  # fmt: skip

    elif not op4:
        return op3(op2(op1(op0(value))))  # fmt: skip

    elif not op5:
        return op4(op3(op2(op1(op0(value)))))  # fmt: skip

    elif not op6:
        return op5(op4(op3(op2(op1(op0(value))))))  # fmt: skip

    elif not op7:
        return op6(op5(op4(op3(op2(op1(op0(value)))))))  # fmt: skip

    elif not op8:
        return op7(op6(op5(op4(op3(op2(op1(op0(value))))))))  # fmt: skip

    elif not op9:
        return op8(op7(op6(op5(op4(op3(op2(op1(op0(value)))))))))  # fmt: skip

    elif not op10:
        return op9(op8(op7(op6(op5(op4(op3(op2(op1(op0(value))))))))))  # fmt: skip

    elif not op11:
        return op10(op9(op8(op7(op6(op5(op4(op3(op2(op1(op0(value)))))))))))  # fmt: skip

    elif not op12:
        return op11(op10(op9(op8(op7(op6(op5(op4(op3(op2(op1(op0(value))))))))))))  # fmt: skip

    elif not op13:
        return op12(op11(op10(op9(op8(op7(op6(op5(op4(op3(op2(op1(op0(value)))))))))))))  # fmt: skip

    elif not op14:
        return op13(op12(op11(op10(op9(op8(op7(op6(op5(op4(op3(op2(op1(op0(value))))))))))))))  # fmt: skip

    elif not op15:
        return op14(op13(op12(op11(op10(op9(op8(op7(op6(op5(op4(op3(op2(op1(op0(value)))))))))))))))  # fmt: skip

    elif not op16:
        return op15(op14(op13(op12(op11(op10(op9(op8(op7(op6(op5(op4(op3(op2(op1(op0(value))))))))))))))))  # fmt: skip

    elif not op17:
        return op16(op15(op14(op13(op12(op11(op10(op9(op8(op7(op6(op5(op4(op3(op2(op1(op0(value)))))))))))))))))  # fmt: skip

    elif not op18:
        return op17(op16(op15(op14(op13(op12(op11(op10(op9(op8(op7(op6(op5(op4(op3(op2(op1(op0(value))))))))))))))))))  # fmt: skip

    elif not op19:
        return op18(op17(op16(op15(op14(op13(op12(op11(op10(op9(op8(op7(op6(op5(op4(op3(op2(op1(op0(value)))))))))))))))))))  # fmt: skip
    else:
        return op19(op18(op17(op16(op15(op14(op13(op12(op11(op10(op9(op8(op7(op6(op5(op4(op3(op2(op1(op0(value))))))))))))))))))))  # fmt: skip
