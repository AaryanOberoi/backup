# things.py

# Let's get this party started!
import falcon
import json
# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.


class ThingsResource(object):  # creates a class ThingsResource
    def on_get(self, req, resp):  # Request and Response are defined
        """Handles GET requests"""
        print('Success')  # Reply from Server every time a request is sent
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = ('\nTwo things awe me most, the starry sky '
                     'above me and the moral law within me.\n'
                     '\n'
                     '    ~ Immanuel Kant\n\n')

    def on_post(self, req, resp):
        print("Hello World")
        data = json.loads(req.stream.read().decode('utf-8'))
        # output the data, we could write it to persistent storage here
        print(data)


# falcon.API instances are callable WSGI apps
app = falcon.API()
# Resources are represented by long-lived class instances
things = ThingsResource()
# things will handle all requests to the '/things' URL path
app.add_route('/', things)  # URL which should be called to send request
