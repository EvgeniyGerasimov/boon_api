USER_CREATED = {
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "userRegistration": {
          "type": "object",
          "properties": {
            "errors": {
             
            },
            "profileCreated": {
              
            },
            "viewer": {
              "type": "object",
              "properties": {
                "accessToken": {
                 
                },
                "ip": {
                  
                },
                "profile": {
                  "type": "object",
                  "properties": {
                    "email": {
                      
                    },
                    "id": {
                      
                    }
                  },
                  "required": [
                    "email",
                    "id"
                  ]
                }
              },
              "required": [
                "accessToken",
                "ip",
                "profile"
              ]
            }
          },
          "required": [
            "errors",
            "profileCreated",
            "viewer"
          ]
        }
      },
      "required": [
        "userRegistration"
      ]
    }
  },
  "required": [
    "data"
  ]
}