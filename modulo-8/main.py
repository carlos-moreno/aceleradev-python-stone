
doc = '''
#%RAML 1.0
title: Challenge Documentation API
documentation:
  - title: Codenation API
    content: Model of api documentation using the RAML format.
version: v1
mediaType: application/json
protocols: [ HTTP, HTTPS ]

securitySchemes:
  JWT:
    description: Authentic this to any method that needs a valid JWT.
    type: x-{other}
    describedBy:
      headers:
        Authorization:
            description: X-AuthToken
            type: string
            required: true
      responses:
        201:
          body: 
            application/json:
              description: Token gerado
        400:
          body: 
            application/json:
              description: Token expirado
    settings:
      signatures: ['HS256']
types:
  Auth:
    type: object
    discriminator: token
    properties:
      token : string
  Agent:
    type: object
    discriminator: agent
    properties:
      agent_id:
        type: integer
        required: true
        example: 1
      name:
        type: string
        required: true
        example: "name example"
      status:
        type: boolean
        required: true
        example: true
      environment:
        type: string
        required: true
        example: "environment example"
      version:
        type: string
        required: true
        example: "versi"
      address:
        type: string
        required: true
        example: "address example"
      user_id:
        type: integer
        required: true
        example: 1
    example:
      agent_id: 1
      user_id: 1
      name: "name example"
      status: true
      environment: "environment example"
      version: "versi"
      address: "address example"
  Event:
    type: object
    discriminator: event
    properties:
      event_id:
        type: integer
        required: true
        example: 1
      agent_id:
        type: integer
        required: true
        example: 1
      level:
        type: string
        required: true
        example: "level example"
      payload:
        type: string
        required: true
        example: "payload example"
      shelved:
        type: boolean
        required: true
        example: true
      date:
        type: datetime
        required: true
        example: "2018-11-26T16:17:18Z"
    example:
      event_id: 1
      agent_id: 1
      level: "level example"
      data: "payload example"
      shelve: true
  Group:
    type: object
    discriminator: group
    properties:
      group_id:
        type: integer
        required: true
        example: 1
      name:
        type: string
        required: true
        example: "name example"
    example:
      group_id: 1
      name: "group example"
  User:
    type: object
    discriminator: user
    properties:
      user_id:
        type: integer
        required: true
        example: 1
      name:
        type: string
        required: true
        example: "name example"
      email:
        type: string
        required: true
        example: "email@example.com"
      last_login:
        type: date-only
        required: true
        example: "2019-11-20"
      group_id: 
        type: string
        required: true
        example: 1 
  Response:
    discriminator: response
    properties:
      mensagem:
        type: string
        example: "mensagem example"
/auth/token:
  post:
    description: Return JWT
    securedBy: JWT
    body:
        application/json:
          type: Auth
          username: string
          password: string
    responses: 
      201:
        body:
          application/json:
            example: {
                      "token": "token gerado"
                     }
      400:
        body:
          application/json:
            example: {
                      "message": "Token expirado."
                     }
/agents:
  description: Agents endpoint.
  get:
    description: Get a list of agents.
    securedBy: JWT
    responses:
      200:
        body: 
          application/json:
            example: [{
                      "agent_id": 1,
                      "name": "string",
                      "status": true,
                      "environment": "string",
                      "version": "string",
                      "address": "198.51.100.42",
                      "user_id": 1
                     }]
      401:
        body:
          application/json:
            example: {
                      "message": "UnauthorizedError."
                     }
  post:
    description: Add a new agent.
    securedBy: JWT
    body:
      application/json:
        example: {
                  "agent_id": 1,
                  "name": "string",
                  "status": true,
                  "environment": "string",
                  "version": "string",
                  "address": "198.51.100.42",
                  "user_id": 1
                }
    responses:
      201:
        body:
          application/json:
            example: {
                      "agent_id": 1,
                      "name": "string",
                      "status": true,
                      "environment": "string",
                      "version": "string",
                      "address": "198.51.100.42",
                      "user_id": 1
                    }
      401:
        body:
          application/json:
            example: {
                      "message": "UnauthorizedError."
                     }
  /{id}:
    uriParameters:
      id:
        description: The Agent identifier.
        type: string
    get:
      description: Gets a specific agent.
      securedBy: JWT
      responses:
        200:
          description: Returns the specific agent.
          body: 
            application/json:
              example: {
                        "agent_id": 1,
                        "name": "string",
                        "status": true,
                        "environment": "string",
                        "version": "string",
                        "address": "198.51.100.42",
                        "user_id": 1
                       }
        401:
          body:
            application/json:
              example: {
                        "message": "UnauthorizedError."
                       }
        404:
          body:
            application/json:
              example: {
                        "message": "Not found."
                       }
    put:
      description: Updates an already created agent.
      securedBy: JWT
      responses:
        200:
          description: Returns the updated agent.
          body: 
            application/json:
              example: {
                        "agent_id": 1,
                        "name": "string",
                        "status": false,
                        "environment": "string",
                        "version": "string",
                        "address": "198.51.100.42",
                        "user_id": 1
                       }
        401:
          body:
            application/json:
              example: {
                        "message": "UnauthorizedError."
                       }
        404:
          body:
            application/json:
              example: {
                        "message": "Not found."
                       }
            
    delete:
      description: Deletes the agent.
      securedBy: JWT
      responses:
        200:
          description: Confirms the deletion.
          body:
            application/json:
              example: {
                        "message": "Agent deleted"
                       }
        401:
          body:
            application/json:
              example: {
                        "message": "UnauthorizedError."
                       }
        404:
          body:
            application/json:
              example: {
                        "message": "Not found."
                       }
  /{id}/events:
    description: Events endpoint.
    get:
      description: Get a list of events.
      securedBy: JWT
      responses:
        200:
          body:
            type: Event[]
        401:
          body:
            application/json:
              example: {
                        "message": "UnauthorizedError."
                       }
        404:
          body:
            application/json:
              example: {
                        "message": "Not found."
                       }
    post:
      description: Add a new event.
      securedBy: JWT
      body:
        application/json:
          example: {
                    "event_id": 1,
                    "agent_id": 1,
                    "level": "level example",
                    "data": "payload example",
                    "shelve": true
                   }
        201:
          body:
            type: Response
            example:
              mensagem: Created
        401:
          body:
            application/json:
              example: {
                        "message": "UnauthorizedError."
                       }
        404:
          body:
            application/json:
              example: {
                        "message": "Not found."
                       }
    put:
      description: Updates an already created event.
      securedBy: JWT
      body:
        type: Event
        200:
          body:
            type: Response
            example:
              mensagem: Created
        401:
          body:
            application/json:
              example: {
                        "message": "UnauthorizedError."
                       }
        404:
          body:
            application/json:
              example: {
                        "message": "Not found."
                       }
      responses:
        200:
          body:
            type: Event
        401:
          body:
            application/json:
              example: {
                        "message": "UnauthorizedError."
                       }
        404:
          body:
            application/json:
              example: {
                        "message": "Not found."
                       }
    delete:
      description: Deletes the event.
      securedBy: JWT
      body: 
        application/json:
          properties: 
            example: {
              }
        200:
          body:
            type: Response
            example:
              mensagem: Created
        401:
          body:
            application/json:
              example: {
                        "message": "UnauthorizedError."
                       }
        404:
          body:
            application/json:
              example: {
                        "message": "Not found."
                       }
      responses:
        200:
          body:
            type: Response
            example:
              mensagem: Created
        401:
          body:
            application/json:
              example: {
                        "message": "UnauthorizedError."
                       }
        404:
          body:
            application/json:
              example: {
                        "message": "Not found."
                       }
/groups:
  description: Groups endpoint.
  get:
    description: Get a list of groups.
    securedBy: JWT
    responses:
      200:
        body:
          type: Group[]
      401:
        body:
          application/json:
            example: {
                      "message": "UnauthorizedError."
                     }
  post:
    description: Add a new group.
    securedBy: JWT
    body:
      application/json:
        properties: 
          example: {
              "group_id": 1,
              "name": "group"
            }
        example: {
              "group_id": 1,
              "name": "group"
            }
    responses:
      201:
        body:
          type: Group
      401:
        body:
          application/json:
            example: {
                      "message": "UnauthorizedError."
                     }
      404:
        body:
          application/json:
            example: {
                      "message": "Not found."
                     }
  /{id}:
    uriParameters:
      id:
        description: The Group identifier.
        type: string
    get:
      description: Gets a specific group.
      securedBy: JWT
      responses:
        200:
          body:
            type: Group[]
        401:
          body:
            application/json:
              example: {
                        "message": "UnauthorizedError."
                       }
        404:
          body:
            application/json:
              example: {
                        "message": "Not found."
                       }
    put:
      description: Updates an already created group.
      securedBy: JWT
      body:
        type: Group
        200:
          body:
            type: Response
            example:
              mensagem: Created
        401:
          body:
            application/json:
              example: {
                        "message": "UnauthorizedError."
                       }
        404:
          body:
            application/json:
              example: {
                        "message": "Not found."
                       }
      responses:
        200:
          body:
            type: Group
        401:
          body:
            application/json:
              example: {
                        "message": "UnauthorizedError."
                       }
        404:
          body:
            application/json:
              example: {
                        "message": "Not found."
                       }
    delete:
      description: Deletes the group.
      securedBy: JWT
      responses:
        204:
          body:
            type: Response
            example:
              mensagem: Excluído com sucesso
        400:
          body:
            application/json:
              example: {
                        "message": "Bad request."
                       }
        401:
          body:
            application/json:
              example: {
                        "message": "UnauthorizedError."
                       }
        404:
          body:
            application/json:
              example: {
                        "message": "Not found."
                       }
/users:
  description: Users endpoint.
  get:
    description: Get a list of users.
    securedBy: JWT
    responses:
      200:
        body:
          type: User[]
      401:
        body:
          application/json:
            example: {
                      "message": "UnauthorizedError."
                     }
  post:
    description: Add a new user.
    securedBy: JWT
    body:
      application/json:
        properties:
          example: {
              "user_id": 1,
              "name": "name",
              "email": "email",
              "last_login": "2019-11-20",
              "group_id": 1
            }
    responses:
      201:
        body:
          type: User
      401:
        body:
          type: Response
          example:
            mensagem: Unauthorized
      404:
        body:
          type: Response
          example:
            mensagem: Bad Request
  /{id}:
    uriParameters:
      id:
        description: The User identifier.
        type: string
    get:
      description: Gets a specific user.
      securedBy: JWT
      responses:
        200:
          body:
            type: User[]
        401:
          body:
            type: Response
            example:
              mensagem: Unauthorized
        404:
          body:
            type: Response
            example:
              mensagem: Bad Request
    put:
      description: Updates an already created user.
      securedBy: JWT
      body:
        type: User
        200:
          body:
            type: Response
            example:
              mensagem: Created
        401:
          body:
            type: Response
            example:
              mensagem: Unauthorized
        404:
          body:
            type: Response
            example:
              mensagem: Bad Request
      responses:
        200:
          body:
            type: User
        401:
          body:
            type: Response
            example:
              mensagem: Unauthorized
        404:
          body:
            type: Response
            example:
              mensagem: Bad Request
    delete:
      description: Deletes the user.
      securedBy: JWT
      responses:
        200:
          body:
            type: Response
            example:
              mensagem: Excluído com sucesso
        401:
          body:
            type: Response
            example:
              mensagem: Unauthorized
        404:
          body:
            type: Response
            example:
              mensagem: Bad Request
'''
