# Crawlers

This program contains 2 crawlers for crawling yelp profiles.  
Supported sites:
  - US (https://www.yelp.com)
  - PT (https://www.yelp.pt/)

## Installation

1. Setup these environment variables in `crawlers/.env` file:
```
ENVIRONMENT
```

2. Install dependencies from `Pipfile`
```
pipenv install
```

3. Run shell in virtual environment
```
pipenv shell
```

# Usage

You can run the program with two CLI options:
  - `--list-url` (crawl only one profile)
  - `--profile-url` (crawl all profiles from list)

# Example

```
python -m crawlers.main --profile-url=https://www.yelp.com/biz/nespresso-boutique-new-york-6
```
