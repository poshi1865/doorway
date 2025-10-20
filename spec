### What is the problem this app solves?
- Sending requests to different llms through a common api.
- Getting around rate limits with the help of multiple providers.
- Having a config file for all your models and providers.
- Tracking input/output tokens and costs. Tracking the actual content of the request and response (if the user wants).

### What we DO NOT offer:
- Access to llm providers (like an openrouter does).
- Retry mechanisms.

### Usage flow:
1. User sends a request to our api. Here they pass an llm, and a body in the openai format.
2. We convert the request to google/claude format if need be.
3. We figure out which provider (vertex/google genai/anthropic/bedrock/azure_openai/openai) to route the request to. We also track input tokens at this point. And calculate input cost. In case all providers are unavailable, we send a "api unavailable/rate limited etc." message back to the client.
4. Provided a provider is available, we send the request forward. We get the response and send/stream it back to the client in the oai format. We also track output tokens and cost.
5. All metrics for observability are written to a db provided by the client, or to sqlite by default.

### Configuration (models, providers, provider keys, fallback order etc.)
1. The user will create a config in a format we decide and send it with each request. This will of course be a one-time config with the sdk.

### Observability
1. We fetch all data from the db, and put it onto a dashboard with some charts and graphs.
