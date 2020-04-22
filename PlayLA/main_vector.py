from LApackage.Vector import Vector

if __name__ == "__main__":
    vec = Vector([1,2,3])
    print(len(vec))
    print("vec[0] = {}, vec[1] = {}".format(vec[0], vec[1]))

    print("vec + vec = {}".format(vec + vec))
    print("vec - vec = {}".format(vec - vec))
    print("-2 * vec = {}".format(-2 * vec))
    print("vec * -2 = {}".format(vec * -2))
    print("+{} = {}".format(vec, +vec))
    print("-{} = {}".format(vec, -vec))

    vec_zero = Vector.zero(3)
    print(vec_zero)
    print("{} + {} = {}".format(vec, vec_zero, vec + vec_zero))

    print("norm({}) = {}".format(vec, vec.norm()))
    print("norm({}) = {}".format(vec_zero, vec_zero.norm()))

    print("normalize {} is {}".format(vec, vec.normalize()))
    print("norm of normalize: {}".format(vec.normalize().norm()))



