def hello(**kwargs):
    # print("Hello " + kwargs['first'] + " " + kwargs['last'])
    print("hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")

hello(title="Mr.", first="Yure", last="Nóbrega")