# Application Architecture

Just going over a high level overview and differenet concepts so that I can know what exactly to look at for future lessons

We as developers write code that gets sent to a server that then runs the code

The code is built and then deployed, once this is done it gets sent to the server

We can assume that a server is just a computer that is able to run the code and deploy it 

Our server also needs to store the data, so we need something like an external storage system, this can be like a :
- database
- data center
- anything really

We can assume that our storage is not running on the same storage but is rather being run seperately and is connected over the network

## External POV

As a user that wants to use our software
- the user sends a request to the server
- the server sends them the HTML and JS code in order to give them what they need
- API requests return something like a JSON format

What if there are many users? what is the bottleneck?
- if CPU is slowing us down we can get a better CPU
- if its the ram we can get more ram so the server can do more

This is an example of vertical scaling. We make this one single system better by making it better, we grow this one to be larger

### IT CAN BE HARDWARE BUT IT USUALLY IS MORE THAN THAT, IT IS ***NETWORK***

For growing our systen we can do ***Horizontal Scaling***

Horizontal scaling is using multiple servers to run our code

This way we can handle the most amount of requests at the same time

The problem with this is that:
- when a user makes a request, what server do we send it to?

This is where we use a Load Balancer

a Load balancer will be covered more in future lessons but for now it:
- handles requests and delegates what needs to be done to different servers
- ensures there are no single points of failure
- makes sure there is a balanced amount of traffic 


we can also use log statements to track how our builds and deployments are working

this log helps us track and manage everything

we can have an external service handle this for us, could be something just like a logger

the user never interacts with this, but us as developer uses this and grows using this

we can set up an alert service such that

if we parse the logs to keep track of certain metrics,

if metric A drops from 100% working to 95% running, we get alerted and we can run to fix it 

before it grows an larger OR before a user has to inform us as that is the absolute worst case situation