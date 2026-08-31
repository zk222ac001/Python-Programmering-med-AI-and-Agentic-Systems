# Pluto's Poetic Journey

Python exercises for reading a news article, extracting key topics, generating a four-line poem, and saving the result to a text file.

## Exercise 1: Read the News Article

```python
def read_article(text_file):
    # Open the file in read mode
    f = open(text_file, "r")

    # Read the contents
    contents = f.read()

    # Close the file
    f.close()

    # Return the contents
    return contents


# Read and print the article
news_article = read_article("news_article.txt")
print(news_article)
```

## Exercise 2: Extract Key Topics

Create a prompt that asks the LLM to identify exactly three key topics from the article.

```python
prompt = f"""
Read the contents below and extract the key topics discussed in it.
Provide exactly 3 key topics.

Each topic should not be more than 8 words.
Provide each topic on a new line.

Article:
{news_article}

Output Format:
topic_1
topic_2
topic_3
"""

response = get_llm_response(prompt)

print(response)
```

Store the three topics in a Python list.

```python
key_topics = [
    "New Horizons exploration of Pluto",
    "Pluto's surprising geological activity",
    "Future exploration beyond Pluto"
]

print_formatted_list(key_topics)
```

Test the solution:

```python
test_your_code.exercise_2(key_topics)
```

## Exercise 3: Create `topics_to_use`

Create a list of dictionaries containing each topic and a Boolean value indicating whether the topic should be used in the poem.

```python
topics_to_use = [
    {
        "Topic 1": key_topics[0],
        "to_use": True
    },
    {
        "Topic 2": key_topics[1],
        "to_use": True
    },
    {
        "Topic 3": key_topics[2],
        "to_use": False
    }
]

print_formatted_list_of_dict(topics_to_use)
```

Test the solution:

```python
test_your_code.exercise_3(topics_to_use, key_topics)
```

## Exercise 4: Generate a Four-Line Poem

Create a prompt containing the `topics_to_use` list and ask the LLM to generate a poem with exactly four lines.

```python
prompt = f"""
Using the topics from the following list:

{topics_to_use}

Write a poem using the topics where "to_use" is True.

The poem must contain exactly 4 lines.
"""

print(prompt)
```

Test the prompt:

```python
test_your_code.exercise_4(prompt, topics_to_use)
```

Generate and display the poem:

```python
poem = get_llm_response(prompt)

print(poem)
```

## Exercise 5: Save the Poem

Create a function that saves the generated poem in a file named `poem.txt`.

```python
def save_to_file(contents_to_save):
    # Open or create poem.txt in write mode
    f = open("poem.txt", "w")

    # Write the contents into the file
    f.write(contents_to_save)

    # Close the file
    f.close()
```

Test the function:

```python
test_your_code.exercise_5(save_to_file)
```

Save the generated poem:

```python
save_to_file(poem)
```

## Complete Workflow

The program performs the following tasks:

1. Reads the Pluto news article from `news_article.txt`.
2. Uses an LLM to extract three key topics.
3. Stores the topics in a Python list.
4. Selects which topics should be used.
5. Uses the selected topics to generate a four-line poem.
6. Saves the generated poem to `poem.txt`.