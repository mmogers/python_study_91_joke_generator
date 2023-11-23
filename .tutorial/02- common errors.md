# Common Errors

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

## Capitalization matters!

👉 What's the problem here?

```python
import requests, json

result = requests.get("https://icanhazdadjoke.com/", headers={"accept":"application/json"}) 

joke = result.json()
print(joke["joke"])
```

<details> <summary> 👀 Answer </summary>
I got my capitalization wrong on 'Accept' (line 3).
  
```python
import requests, json

result = requests.get("https://icanhazdadjoke.com/", headers={"Accept":"application/json"}) 

joke = result.json()
print(joke["joke"])
```

</details>

