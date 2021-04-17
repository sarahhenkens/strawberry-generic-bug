## Install

```
poetry install
```

## Run

```
poetry run strawberry server app.schema
```

## Error message

```
  File "./app.py", line 26, in <module>
    schema = strawberry.Schema(query=Query)
  File "/Users/sarah/projects/generic-bug-strawberry/.venv/lib/python3.9/site-packages/strawberry/schema/schema.py", line 64, in __init__
    self._schema = GraphQLSchema(
  File "/Users/sarah/projects/generic-bug-strawberry/.venv/lib/python3.9/site-packages/graphql/type/schema.py", line 208, in __init__
    collect_referenced_types(query)
  File "/Users/sarah/projects/generic-bug-strawberry/.venv/lib/python3.9/site-packages/graphql/type/schema.py", line 422, in collect_referenced_types
    for field in named_type.fields.values():
  File "/Users/sarah/.pyenv/versions/3.9.1/lib/python3.9/functools.py", line 969, in __get__
    val = self.func(instance)
  File "/Users/sarah/projects/generic-bug-strawberry/.venv/lib/python3.9/site-packages/graphql/type/definition.py", line 760, in fields
    raise TypeError(f"{self.name} fields cannot be resolved. {error}")
TypeError: Query fields cannot be resolved. The type "Book" of the field "None" is generic, but no type has been passed
```
