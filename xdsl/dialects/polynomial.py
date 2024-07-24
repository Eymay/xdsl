
from xdsl.dialects.builtin import IntegerAttr
from xdsl.ir import Dialect

from xdsl.ir.core import ParametrizedAttribute, TypeAttribute
from xdsl.irdl import (
    IRDLOperation,
    irdl_op_definition,
)
from xdsl.irdl.attributes import ParameterDef, irdl_attr_definition
from xdsl.irdl.constraints import AnyOf
from xdsl.irdl.operations import result_def

@irdl_attr_definition
class IntPolynomialAttr(ParametrizedAttribute):
    """
    https://mlir.llvm.org/docs/Dialects/PolynomialDialect/#intpolynomialattr
    """

    name = "polnomial.int_polynomial"

    #TODO get monomials list as a parameter?
    polynomial: ParameterDef[]

@irdl_attr_definition
class RingAttr(ParametrizedAttribute):
    """
    https://mlir.llvm.org/docs/Dialects/PolynomialDialect/#ringattr
    """

    name = "polynomial.ring"

    coefficientType: ParameterDef[TypeAttribute]
    coefficientModulus: ParameterDef[IntegerAttr]
    polynomialModulus: ParameterDef[IntPolynomialAttr]


@irdl_attr_definition
class PolynomialType(ParametrizedAttribute, TypeAttribute):
    """
    https://mlir.llvm.org/docs/Dialects/PolynomialDialect/#polynomialtype
    """

    name = "polynomial.polynomial"

@irdl_op_definition
class ConstantOp(IRDLOperation):

    name = "polynomial.constant"

    value = attr_def(AnyOf(
        # float_polynomial
        #or int_polynomial
        ))

    output = result_def(# an element of a polynomial ring
                        )





Polynomial = Dialect(
        "polynomial",
        [
            ConstantOp,
        ],
        []
        )
