# Building and Deploying Cloud Native App
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

  *createAdvertisement*: https://funcazuredevprj2.azurewebsites.net/api/createadvertisement <p>
  *deleteAdvertisement*: https://funcazuredevprj2.azurewebsites.net/api/deleteadvertisement <p>
  *getAdvertisement*: https://funcazuredevprj2.azurewebsites.net/api/getadvertisement <p>
  *getAdvertisements*: https://funcazuredevprj2.azurewebsites.net/api/getadvertisements <p>
  *getPost*: https://funcazuredevprj2.azurewebsites.net/api/getpost <p>
  *getPosts*: https://funcazuredevprj2.azurewebsites.net/api/getposts <p>
  *updateAdvertisement*: https://funcazuredevprj2.azurewebsites.net/api/updateadvertisement <p>


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
![](img/2021-06-04-15-20-13.png)

The Logic App Designer
![](img/2021-06-04-15-19-14.png)

Mail was successfully sent
![](img/2021-06-04-15-14-59.png)

### The student should be able to create a custom event grid topic and publish the topic.

##### Event Hub

To evaluate the feature, I have run the followings to set up the services.
```
az eventhubs namespace create --resource-group rg_azuredevprj2 --name azuredevprj2ehns --location centralus --sku Standard --maximum-throughput-units 1 --enable-auto-inflate true
az eventhubs eventhub create --resource-group rg_azuredevprj2 --namespace-name azuredevprj2ehns --name azuredevprjeh --message-retention 1 --partition-count 1
az storage account create --name stracazuredevprj2 --resource-group rg_azuredevprj2 --location centralus --sku Standard_LRS
az functionapp create --functions-version 3 --resource-group rg_azuredevprj2 --name funcazuredevprj2 --storage-account stracazuredevprj2 --os-type Linux --consumption-plan-location centralus --runtime python --runtime-version 3.8
```

Following is the screenshot from the event hub, after sending some events.

![](img/2021-06-06-23-54-32.png)


As below, created a fundtion app to be triggered by even hub.
The connection string is set as an environment variable *azuredevprj2ehns_RootManageSharedAccessKey_EVENTHUB* in the application settings in the function app as below.

![](img/2021-06-07-00-04-06.png)

This can be referenced as below on the *connection* part in the *function.json*.

```
{
  "scriptFile": "__init__.py",
  "bindings": [
    {
      "type": "eventHubTrigger",
      "name": "events",
      "direction": "in",
      "eventHubName": "azuredevprjeh",
      "connection": "azuredevprj2ehns_RootManageSharedAccessKey_EVENTHUB",
      "cardinality": "many",
      "consumerGroup": "$Default",
      "dataType": "binary"
    }
  ]
}
```

Following is the function triggered by the events in the event hub.

![](img/2021-06-07-00-00-48.png)


##### Event Grid



### The student should be able to add the connection string of the event hub to the Azure Function.


![](img/2021-06-05-12-59-00.png)

![](img/2021-06-05-13-04-10.png)

![](img/2021-06-05-13-02-07.png)

![](img/2021-06-05-13-12-25.png)


## Deploying Your Application

### The student should be able to deploy their Neighborly web application on Azure App Service.

Azure portal where Flask app deployed
![](img/2021-06-04-13-26-55.png)

### The student should be able to containerize their Flask application with Dockerfile.

Container Registry

![](img/2021-06-04-13-14-00.png)


### The code demonstrates an automated pipeline to spin Kubernetes services in Azure.

![](img/2021-06-05-16-41-52.png)

![](img/2021-06-05-16-37-21.png)