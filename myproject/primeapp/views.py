import datetime
import json

from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse

# Create your views here.
from primeapp.utils import printPrime, prime_eratosthenes, prime_Atkins
from primeapp import constant
from time import time


def generate_prime_parameters(request):
    """
    Generate a list of primes on the basis of the upper bound received
    in request payload.
    """
    payload = json.loads(request.body.decode('utf-8'))

    timestamp = datetime.datetime.now()
    method = payload.get("method", "")
    requested_upper_bound = payload.get("upper_bound", "")

    requested_upper_bound = int(float(requested_upper_bound))
    response = {
        "timestamp": timestamp,
        "method": method,
        "requested_range": {
            "lower_bound": 2,
            "upper_bound": requested_upper_bound
        },
        "max_allowed_upper_bound": constant.UPPER_BOUND
    }

    primes_list = []
    if requested_upper_bound > constant.UPPER_BOUND:
        response.update({
            "primes": primes_list,
            "status": "FAILED",
            "msg": f"Max allowed upper bound exceeded. Prime Numbers can be generated up to a maximum of {constant.UPPER_BOUND}"
        })
    else:
        if method == "SOE":
            start = time()
            primes_list = prime_eratosthenes(requested_upper_bound)
            execution_time = time() - start
            response.update({
                "primes": primes_list,
                "status": "SUCCESS",
                "execution_time": execution_time
            })
        elif method == "NAIVE":
            start = time()
            primes_list = printPrime(requested_upper_bound)
            execution_time = time() - start
            response.update({
                "primes": primes_list,
                "status": "SUCCESS",
                "execution_time": execution_time
            })
        elif method == "ATKINS":
            start = time()
            primes_list = prime_Atkins(requested_upper_bound)
            execution_time = time() - start
            response.update({
                "primes": primes_list,
                "status": "SUCCESS",
                "execution_time": execution_time
            })
        else:
            response.update({
                "primes": primes_list,
                "status": "FAILED",
                "msg": "Unsupported generation method. Supported methods are 'SOE', 'NAIVE' and 'ATKINS'"
            })
    primes_list_len = len(response.get("primes", []))

    response.update({
        "no_of_primes": primes_list_len
    })
    return JsonResponse(response)
