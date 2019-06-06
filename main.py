#Importing logger
import logging

LOG = logging.getLogger(__name__)


class printHelloWorld:

    #Function to print Hello world
    def print_helloworld(self):
        print("Hello World!")


try:
    #Instantiating printHelloWorld class
    p = printHelloWorld()
    LOG.info("Calling print hello world function: ")
    p.print_helloworld()

except:
    LOG.info("Error while printing Hello World!!")
    pass

