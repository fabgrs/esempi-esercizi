def function(a):
    print(a)


if __name__ == '__main__':
    i = 10
    words = [1, 2, "ciao", 4, 5, 6]
    for i, elem in enumerate(words):
        print("elemento numero ", i, " ",elem)

    dict = {"a": "aa", "b": "bb"}
    print(dict["a"])
    print(dict.keys())
    print(dict.values())
    function(a=30)
