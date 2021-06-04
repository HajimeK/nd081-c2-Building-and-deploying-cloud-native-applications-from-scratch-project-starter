
## Serverless Functions
### A MongoDB database in Azure CosmosDB service is created and initialized with the sample data provided.

Data stored in Mongo DB

Advertisements

![](img/2021-06-04-13-24-26.png)

Posts

![](img/2021-06-04-13-25-28.png)

Call from the REST API (Visual Studio Code plug-in) also woks.

![](img/2021-06-04-15-23-05.png)

In the portal.
![](img/2021-06-04-15-24-31.png)

### The finished server-side application contains working Azure Functions for HTTP Triggers in Python.

  *createAdvertisement*: https://funcazuredevprj2.azurewebsites.net/api/createadvertisement
  *deleteAdvertisement*: https://funcazuredevprj2.azurewebsites.net/api/deleteadvertisement
  *getAdvertisement*: https://funcazuredevprj2.azurewebsites.net/api/getadvertisement
  *getAdvertisements*: https://funcazuredevprj2.azurewebsites.net/api/getadvertisements
  *getPost*: https://funcazuredevprj2.azurewebsites.net/api/getpost
  *getPosts*: https://funcazuredevprj2.azurewebsites.net/api/getposts
  *updateAdvertisement*: https://funcazuredevprj2.azurewebsites.net/api/updateadvertisement


Functions End Points
![](img/2021-06-04-13-16-27.png)


Followings are the live example from *getAdvertisements* 


![](img/2021-06-04-13-55-09.png)

and *getPosts*


![](img/2021-06-04-13-56-06.png)


### The Azure Functions HTTP Trigger endpoints can connect to MongoDB in Azure CosmosDB service.

See above screenshots.

### The client-side application in Flask should be able to call the live Functions API endpoints that the students published in previous steps.

Accessing the URL (https://azuredevprj2webapp.azurewebsites.net) to get the following result.

![](img/2021-06-04-13-29-15.png)


## Logic Apps & Event Hubs

### The student demonstrates mastery in using Azure Logic App Designer to create a trigger.

Definitions and test run status
![](2021-06-04-15-20-13.png)

The Logic App Designer
![](img/2021-06-04-15-19-14.png)

Mail was successfully sent
![](img/2021-06-04-15-14-59.png)

### The student should be able to create a custom event grid topic and publish the topic.

Under name space *azredevprj2ehns*, an Event Hub *azuredevprj2eh* is created.
![](img/2021-06-04-13-32-33.png)

### The student should be able to add the connection string of the event hub to the Azure Function.

See above in the Shared access policies.
*azredevprj2ehpolicy* is added.

## Deploying Your Application

### The student should be able to deploy their Neighborly web application on Azure App Service.

Azure portal where Flask app deployed
![](img/2021-06-04-13-26-55.png)

### The student should be able to containerize their Flask application with Dockerfile.

Container Registry

![](img/2021-06-04-13-14-00.png)


### The code demonstrates an automated pipeline to spin Kubernetes services in Azure.

![](img/2021-06-04-13-10-43.png)

