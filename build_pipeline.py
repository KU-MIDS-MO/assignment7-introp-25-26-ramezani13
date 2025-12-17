def build_pipeline(operation_names):
    operations = {
        "double": lambda x: x * 2,
        "triple": lambda x: x * 3,
        "square": lambda x: x * x
    }

    for name in operation_names:
        if name not in operations:
            raise KeyError(name)

    def pipeline(x):
        value = x
        for name in operation_names:
            value = operations[name](value)
        return value

    return pipeline

f = build_pipeline(["double", "square"])
result = f(1)
print(result)


