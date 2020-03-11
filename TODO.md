# TODO

## web app

### user ratings

- logic to update score when changing from, e.g., like to dislike or vice versa
- update ratings/buttons in UI when clicking

### authentication

- integrated with REST APIs

## REST APIs

### user authentication

- integrated with web app

## Recommender sys

### Filter articles shown to user

- only recommend articles to the user that are "new" and "potentially relevant" to the user
    - measuring "new": never looked at before?
    - measuring "relevant": ?

### Padding strategy

- what's the influence of padding sentences to longest?

## Airflow

### Failing DAG for arxiv due to empty article/response

```
[2020-03-08 08:45:50,013] {{taskinstance.py:1088}} ERROR - Expecting value: line 1 column 1 (char 0)
Traceback (most recent call last):
  File "/usr/local/lib/python3.7/site-packages/airflow/models/taskinstance.py", line 955, in _run_raw_task
    result = task_copy.execute(context=context)
  File "/usr/local/lib/python3.7/site-packages/airflow/operators/python_operator.py", line 113, in execute
    return_value = self.execute_callable()
  File "/usr/local/lib/python3.7/site-packages/airflow/operators/python_operator.py", line 118, in execute_callable
    return self.python_callable(*self.op_args, **self.op_kwargs)
  File "/usr/local/airflow/dags/parse_arxiv.py", line 56, in parse_arxix
    f"PUT failed with code {put_r.status_code} {put_r.json()} for:{os.linesep}{payload}"
  File "/usr/local/lib/python3.7/site-packages/requests/models.py", line 897, in json
    return complexjson.loads(self.text, **kwargs)
  File "/usr/local/lib/python3.7/json/__init__.py", line 348, in loads
    return _default_decoder.decode(s)
  File "/usr/local/lib/python3.7/json/decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "/usr/local/lib/python3.7/json/decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
[2020-03-08 08:45:50,017] {{taskinstance.py:1117}} INFO - All retries failed; marking task as FAILED
```
