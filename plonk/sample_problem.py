from .copy_constraint import find_permutation
from .constraint import add_mul_constraint, add_add_constraint, add_constant_constraint


def gen_witness(x, y, z):
    a = [x, x * x, y, y * y, x * x + y * y]
    b = [x, 1, y, 1, 1]
    c = [x * x, x * x, y * y, y * y, z * z]

    return (a, b, c)


def is_satisfied_witness(a, b, c):
    assert a[0] * b[0] == c[0]
    assert a[1] == c[1]
    assert a[2] * b[2] == c[2]
    assert a[3] == c[3]
    assert a[4] == c[4]


def gen_constraints():
    # Prove that I know x, y, z such that x^2 + y^2 == z^2

    # init constraints
    Ql = []
    Qr = []
    Qm = []
    Qo = []
    Qc = []

    # set constraints
    Ql, Qr, Qm, Qo, Qc = add_mul_constraint(Ql, Qr, Qm, Qo, Qc)
    Ql, Qr, Qm, Qo, Qc = add_mul_constraint(Ql, Qr, Qm, Qo, Qc)
    Ql, Qr, Qm, Qo, Qc = add_add_constraint(Ql, Qr, Qm, Qo, Qc)
    Ql, Qr, Qm, Qo, Qc = add_constant_constraint(Ql, Qr, Qm, Qo, Qc, 25)

    return Ql, Qr, Qm, Qo, Qc


def gen_copy_constraints():
    # copy constraints
    # a = [x, x*x, y, y*y, x*x + y*y]
    # b = [x, 1, y, 1, 1]
    # c = [x*x, x*x, y*y, y*y, z*z]
    # inputs = [x, x*x, y, y*y, x*x + y*y,
    #           x, 1, y, 1, 1,
    #           x*x, x*x, y*y, y*y, z*z]

    copy_constraints = [5, 10, 11, 3, 7, 12, 0, 6, 2, 8, 4, 9, 1, 13, 14]

    eval_domain = range(0, len(copy_constraints))

    x_a_prime = find_permutation(copy_constraints[0:5], eval_domain[0:5])
    x_b_prime = find_permutation(copy_constraints[5:10], eval_domain[5:10])
    x_c_prime = find_permutation(copy_constraints[10:15], eval_domain[10:15])

    return x_a_prime, x_b_prime, x_c_prime, copy_constraints


def setup():
    Ql, Qr, Qm, Qo, Qc = gen_constraints()
    perm_x, perm_y, perm_z, copy_constraints = gen_copy_constraints()

    return Ql, Qr, Qm, Qo, Qc, perm_x, perm_y, perm_z, copy_constraints
