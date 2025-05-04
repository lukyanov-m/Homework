def log(filename=None):
    """
    Декоратор записывает в указанный filename файл результат выполнения функции, в случае ошибки запишет эту ошибку
    и принятые функцией параметры. Если filename не указан, выведет информацию в консоль.
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} Ok. Inputs: {args}, {kwargs}. \n"
            except Exception as e:
                message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}. \n"
                if filename:
                    with open(filename, "a") as f:
                        f.write(message)
                else:
                    print(message)
                raise

            if filename:
                with open(filename, "a") as f:
                    f.write(message)
            else:
                print(message)

            return result

        return wrapper

    return decorator
