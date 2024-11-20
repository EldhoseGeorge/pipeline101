import fire

def hello(name="earth"):
    return "hello %s!" %name

if __name__=="__main__":
    fire.Fire(hello)