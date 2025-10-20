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
	Observability - tracking token input/output, cost. We can also track things like number of times rate limits were hit, provider specific traffic etc etc.

## Some decisions:
- API can either be sync or async.
- Use grpc because better streaming.
- Use sqlite as a default database.
