# Implement a Flask backend service that tells whether a number received as a parameter is a prime number or not.
# Use the prior prime number exercise as a starting point. For example,
# a GET request for number 31 is given as: http://127.0.0.1:5000/prime_number/31.
# The response must be in the format of {"Number":31, "isPrime":true}.
from flask import Flask

app = Flask(__name__)


@app.route('/prime_number/<num>')
def isPrime(num):
    ans = True
    flag = True
    num = int(num)
    if num == 1:
        print("the num is not prime")
        ans = False
    else:
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                flag = False
                break
        if flag:
            print("the num is prime")
            ans = True
        else:
            print("the num is not prime")
            ans = False

    response = {

        "Number": num,
        "isPrime": ans
    }
    return response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
