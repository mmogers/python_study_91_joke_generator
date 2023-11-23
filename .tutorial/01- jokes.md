# Funny, eh? Funny, how?


## Dad Jokes

The API we're using today is the awesome [icanhazdadjoke](https://icanhazdadjoke.com/api). Go and check out their API documentation before continuing. Look at the **endpoint** to see the URL to access and the format of the data we'll get back.

👉  Here's the code to get a random dad joke and output it.
**NOTE** - The second argument (`headers=`) in `requests.get()` is really important. It tells the code that we don't want the website back, we want JSON data in a specific format. Sometimes you need to do that.


```python
import requests, json

result = requests.get("https://icanhazdadjoke.com/", headers={"Accept":"application/json"}) # get a random dad joke from the site endpoint and assign to a variable. The second argument (the header request) tells the script to return the json data as a string.

joke = result.json()
print(json.dumps(joke, indent=2))
```
👉 I can change the print statement to just output the joke instead of the whole dictionary.
```python
print(joke["joke"])
```

### The API for this site is a really good one to learn from as it gives lots of great examples of how to import jokes in different formats.

