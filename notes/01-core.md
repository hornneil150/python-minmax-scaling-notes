# Scale values to a unit interval: implementation

## What the example does

Subtract the minimum and divide by the range. A constant series maps to zeros by convention here, and an empty series remains empty.

The public function is `solve(value)`. The JSON input contract can be seen in this concrete example:

```json
[
  10,
  20,
  30
]
```

Expected result:

```json
[
  0.0,
  0.5,
  1.0
]
```

Run `python3 example.py` for the Python representation of the result. `solution.py` contains the full implementation and can also be imported by another script.

## Scope

The function implements exactly the behavior described above. It does not perform network or filesystem access. Python exceptions indicate unsupported input; the next lesson turns them into a command-line error response. Review the limitations before reusing it in an application.
