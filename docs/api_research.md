# Cat Facts API Research

## Why Cat Facts?
- Completely free and publicly documented.
- No API keys required, making it excellent for workshops.
- Provides lightweight JSON responses that are easy to parse live on stage.

## Base URL
```
https://catfact.ninja
```

## Key Endpoints
| Endpoint | Description | Sample Request | Sample Response |
| --- | --- | --- | --- |
| `/fact` | Returns one random fact. | `GET https://catfact.ninja/fact` | ```json
{
  "fact": "Cats have five toes on their front paws.",
  "length": 44
}
``` |
| `/facts` | Returns a paginated list of facts. | `GET https://catfact.ninja/facts?limit=3` | ```json
{
  "current_page": 1,
  "data": [
    {"fact": "Cats sleep 12-16 hours per day.", "length": 36},
    {"fact": "A group of kittens is called a kindle.", "length": 43},
    {"fact": "Adult cats meow only at humans.", "length": 33}
  ],
  "per_page": 3,
  "total": 332
}
``` |
| `/breeds` | Lists cat breeds with metadata. | `GET https://catfact.ninja/breeds?limit=2` | ```json
{
  "current_page": 1,
  "data": [
    {
      "breed": "Abyssinian",
      "country": "Ethiopia",
      "origin": "Natural",
      "coat": "Short",
      "pattern": "Ticked"
    },
    {
      "breed": "Aegean",
      "country": "Greece",
      "origin": "Natural",
      "coat": "Medium",
      "pattern": "Bi- or tri-colored"
    }
  ],
  "per_page": 2,
  "total": 67
}
``` |

## Notes for the Workshop
- The API occasionally rate-limits with HTTP 429 when called rapidly; add retry/backoff logic in production.
- Responses are simple enough to show raw JSON in the IDE’s HTTP client.
- Because the workshop environment may sit behind corporate proxies, have a backup plan (recorded responses or local mock server).
