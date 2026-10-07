# postman

This job lets you import Postman collections via a URL or a local file.

The variables parameter works as follows:

Any variables defined in the collection will be replaced with their values. Additionally, the dialog allows for the provision of a comma-separated list of variables as key-value pairs in the format `key1=value1,key2=value2,...` these variables will have precedence over the collection ones.

## Jobs Structure

```
jobs:
- parameters:    
collectionFile: "/Users/user/postman.yaml"    
collectionUrl: "key1=value1,key2=value2"    
variables: http://TestURL.com/*  
name: "postman"  
type: "postman"
```

###### Possible parameters

[collectionFile:\<String\> (default: null, no collection will be imported)](postman.md#UUID-5a34d02c-c494-ed09-194d-db3a09ea978d_N66a1066db46a9)

Local file containing the Postman collection,

[collectionUrl:\<String\> (default: null, no collection will be imported)](postman.md#id11336)

URL containing the Postman collection,

[variables:\<String\> (default: null, no additional variables will be imported)](postman.md#id11341)

Comma-separated list of variables as key-value pairs in the format `key1=value1,key2=value2,...,` these variables will have precedence over the collection ones
