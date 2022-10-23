# prime_number_generator
 A concise,efficient and robust prime generator written in python language which 
 gives all prime numbers in the range between the number 2 and the upper bound
 (the last number within which the prime numbers should be found).
 # Usage
 A comma delimited array of prime numbers gets returned between the number 2 and the upper bound.
 The method attribute in views.py is used to select the choice of generation strategy
 for prime numbers within the given range.
  1. SOE, a sieve of eratosthenes algorithm
  2. NAIVE, a naive brute force algorithm
  3. ATKINS, a sieve of atkins algorithm
 
 The lower bound is fixed as 2. Since the starting cannot be 1.
 The upper bound parament expect to be an integer within the range 1000000.
 
# Rest API
1. Start the webserver django application
    python manage.py runserver
    http://127.0.0.1:8000/
2. Send a GET Request(using postman)
    http://127.0.0.1:8000/primeg/
3. The server will respond with the following JSON format:
   {
    "timestamp": "2022-10-21T22:22:11.771",
    "method": "ATKINS",
    "requested_range": {
        "lower_bound": 2,
        "upper_bound": 1000000
    },
    "max_allowed_upper_bound": 1000000,
     "primes": [...],
     "status": "SUCCESS",
    "execution_time": 3.707653760910034,
    "no_of_primes": 78498
    }
    
