# strela
A RESTful API around the Arrow library for time manipulation.

## Stre-what?
Cтрела(*Strela*) is the Russian word for "arrow". Seeing that we're wrapping the Arrow library...

## Why?
Arrow happens to be a really good library for datetime manipulation, especially with timezones. But that's kinda lacking
in other languages. And these days, with my experiments in Crystal, I needed an easy way to call Arrow's functionality from Crystal - 
an API wrapper made the most sense.

## What does it support?
For now, it supports basic timezone conversion - you can query a list of all available IANA timezones, and you can pass a timezone,
and Strela converts the current UTC timestamp to that timezone. I'd like to create API endpoints for all of Arrow's features, though,
so hang in there. 

## How can I use this?
You could start by reading some notes I typed up: [*docs.md*](https://github.com/rudimk/strela/blob/master/docs.md)

## Can I help?
Is the Pope Catholic?
Check out the list of issues here. Feel free to submit a PR, and I swear I won't mess around. Or if you'd like to add something, all
yours.

## How can I thank you?
You can always treat me to a nice hot cup of coffee, or a nice wheat lager. Bacon and donuts are acceptable too.
