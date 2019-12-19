
# README

This is an example of Wallarm FAST integration with the DVWA using Selenium tests.

Learn more about FAST:
* [FAST website](https://wallarm.com/products/fast) 
* [FAST documentation](https://docs.fast.wallarm.com/en/)

## How to run tests locally

Install Docker and Docker Compose.

Create your FAST node here:
https://us1.my.wallarm.com/nodes.

Replace WALLARM_API_TOKEN in ./local.sh and run it.

## What is happening

Building your application. In this example, [DVWA - Damn Vulnerable Web Application](http://www.dvwa.co.uk) is used as an example of the vulnerable web application. The build includes a preconfigured database to skip the registration process. This is an equivalent to build stage of your CI/CD pipeline.

```
sudo -E docker-compose build
```

Run the target application. Test environment consists of Wallarm FAST and Selenium. The FAST proxy is used to record baselines.

```
sudo -E docker-compose up -d dvwa fast selenium
```

The next step runs the tests. The 'test' container consists of a Python script with a few selenium tests. This is equivalent to a testing stage of your CD/CD pipeline.

```
sudo -E docker-compose run test
```

Once the functional tests pass, Wallarm FAST is launched to run security tests. Security tests are based on the baselines that have been recorded in the the testing stage.

```
sudo -E docker-compose run --rm -e CI_MODE=testing -e TEST_RUN_URI=http://dvwa:80 fast
```

Finally, the cleanup stage:
```
sudo -E docker-compose down
```

For full FAST documentation, visit https://docs.fast.wallarm.com.
