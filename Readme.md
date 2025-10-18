## v0 features
1. Support for both streaming and non-streaming.
2. Providers we support -
	Azure OpenAI,
	OpenAI,
	Anthropic Claude
3. Features we support -
	CONFIG FILE - YAML. (will contain db uri in addition to the usual stuff)
	Direct passthrough.
	Bulk llm requests - upto a max size. GIMMICK.
	Fallback strategy.
	Observability - tracking token input/output, cost, DON'T TRACK RESPONSE or INPUT. We can also track things like number of times rate limits were hit, provider specific traffic etc etc.

## Data modeling:
Use the openai completions api.
- Create chat completion (no store param).
- No crud on chat completion messages.


## Some decisions:
- API can either be sync or async.
- Use grpc because better streaming.
- Use sqlite as a default database.

3 main modules:
1. Request <-> Response translation engine.
2. Routing engine.
3. Observability (a part of  the routing engine)
	
    {
		model,
		provider,
		input_tokens,
		output_tokens,
		input_cost,
		output_cost,
		request_content (openai format, will only get if this feature is on),
		response_content (openai format, will only get if this feature is on),
		timestamps,
		latency,
	}

CONFIG SCHEMA:
{
	db_uri: optional,
	provider_config: [
		{
			name: "user_defined_name. eg: azure_openai_dev",
			type: enum("azure_oai", "openai", "vertex")
			uri:
			key:
			version:
		}
	],
	fallback_config: [
		
	],
	models: [
		model1 : {
			providers: [vertex, genai],
			fallback_models: [gpt4.1, o3-mini]
		}
		gpt4.1 : {
			providers: [azure openai, openai],
			fallback_models: [gpt4.1, o3-mini]
		}
	]
}
