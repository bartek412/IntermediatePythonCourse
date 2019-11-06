def double(x):
    return 2 * x


def root(x):
    return x ** 2


def negative(x):
    return -x


def div2(x):
    return x / 2


number = 8
transformations = [double, root, div2, negative]
tmp_return_value = number
for transform in transformations:
    tmp_return_value = transform(tmp_return_value)
    print('{}: temporal result is {}'.format(transform.__name__, tmp_return_value))
