# python_elves
Little helpers written in Python

## JQL Composer
The script is used to compose complex JQL queries from a JSON-encoded dictionary of simpler sub-queries.

It will enclose the expansion of sub-queries in parentheses while expanding, in order to ensure the original precedence.

In order to use one query inside another, use the sub-query's name in brackets inside the outer query. See sample.json for an example.